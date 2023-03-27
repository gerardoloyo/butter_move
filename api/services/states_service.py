from flask import jsonify
from api.models.states_model import State
from api import db
import json

class StatesService:
    def __init__(self, abbreviation, normal_commission, premium_commission, iva, base_discount, total_discount, premium_discount):
        self.abbreviation = abbreviation.upper()
        self.normal_commission = normal_commission
        self.premium_commission = premium_commission
        self.iva = iva
        self.base_discount = json.loads(json.dumps(base_discount))
        self.total_discount = json.loads(json.dumps(total_discount))
        self.premium_discount = json.loads(json.dumps(premium_discount))
    

    def add_state(self):
        try:
            state = State(
                abbreviation = self.abbreviation,
                normal_commission = self.normal_commission,
                premium_commission = self.premium_commission,
                iva = self.iva,
                base_discount = self.base_discount,
                total_discount = self.total_discount,
                premium_discount = self.premium_discount
            )
            db.session.add(state)
            db.session.commit()
        except Exception as e:
            return jsonify({'result': 'ERROR', 'message': 'Unexpected error'}), 500

        return jsonify({'result': 'OK', 'message': 'State added sucessfully'}), 201

    
    def update_state(self):
        try:
            current_state = State.query.filter_by(self.abbreviation).first()

            if not current_state:
                return jsonify({'result': 'FAIL', 'message': 'State not found'}), 422

            normal_com = current_state.normal_commission if self.normal_commission is None else self.normal_commission
            premium_com = current_state.premium_commission if self.premium_commission is None else self.premium_commission
            current_state.normal_commission = normal_com
            current_state.premium_commission = premium_com
            current_state.iva = self.iva
            current_state.base_discount = self.base_discount
            current_state.total_discount = self.total_discount
            current_state.premium_discount = self.premium_discount

            db.session.commit()
        except Exception as e:
            return jsonify({'result': 'ERROR', 'message': 'Unexpected error'}), 500
        
        return jsonify({'result': 'OK', 'message': 'State updated successfully'}), 200

