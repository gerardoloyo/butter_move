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
        total_amount = self.base_amount * (1 + commission)

        if self.estimation_type == 'NORMAL':
            if state == 'NY':
                total_amount *= 1.21
            elif state in ('CA', 'AZ') and self.kilometers > 26:
                total_amount *= 0.95
            elif state in ('TX', 'OH'):
                if 20 <= self.kilometers <= 30:
                    total_amount *= 0.97
                elif self.kilometers > 30:
                    total_amount *= 0.95
        elif self.estimation_type == 'PREMIUM':
            if self.kilometers > 25:
                total_amount *= 0.95

        return jsonify({
            'total_amount': round(total_amount, 2),
            'processed_date': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        }), 200


