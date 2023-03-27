from flask import jsonify
from datetime import datetime
from api.models.states_model import State

class EstimationsService:
    def __init__(self, state, estimation_type, kilometers, base_amount):
        self.state = state.upper()
        self.estimation_type = estimation_type.upper()
        self.kilometers = kilometers
        self.base_amount = base_amount

    def calculate_estimation(self):
        try:
            state = State.query.filter_by(abbreviation = self.state).first()
        except Exception as e:
            return jsonify({'result': 'ERROR', 'message': 'Unexpected error'}), 500
        
        if not state:
            return jsonify({'result': 'FAIL', 'message': 'Unsupported state'}), 422

        commission = state.normal_commission if self.estimation_type == 'NORMAL' else state.premium_commission
        total_discount = 0.0
        base_discount = 0.0

        if self.estimation_type == 'NORMAL':
            base_discount = self.get_discount(state.base_discount, self.kilometers)

            if base_discount == 0.0:
                total_discount = self.get_discount(state.total_discount, self.kilometers)
        
        if self.estimation_type == 'PREMIUM':
            total_discount = self.get_discount(state.premium_discount, self.kilometers)
        
        base_amount = self.base_amount * (1 - base_discount)
        total_amount = base_amount * (1 + commission)
        total_with_discount = total_amount * (1 - total_discount)
        total_plus_taxes = total_with_discount * (1 + state.iva)

        return jsonify({
            'total_amount': round(total_plus_taxes, 2),
            'processed_date': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        }), 200
    

    def get_discount(data_json, km_th):
        if data_json['value'] == 0:
            return 0.0

        min_val = data_json.get('min', float('-inf'))
        max_val = data_json.get('max', float('inf'))
        
        min_bound = data_json.get('min_bound', 'inclusive')
        max_bound = data_json.get('max_boundary', 'exclusive')

        if min_bound == 'inclusive':
            min_check = min_val <= km_th
        else:
            min_check = min_val < km_th

        if max_bound == 'inclusive':
            max_check = max_val >= km_th
        else:
            max_check = max_val > km_th

        if min_check and max_check:
            return data_json['value']
        else:
            return 0.0