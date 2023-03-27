from flask import jsonify
from api.models.states_model import State
from api import db

class StatesService:
    def __init__(self, abbreviation, normal_commission, premium_commission):
        self.abbreviation = abbreviation
        self.normal_commission = normal_commission
        self.premium_commission = premium_commission
    

    def add_state(self):
        try:
            state = State(
                abbreviation = self.abbreviation,
                normal_commission = self.normal_commission,
                premium_commission = self.premium_commission 
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

            db.session.commit()
        except Exception as e:
            return jsonify({'result': 'ERROR', 'message': 'Unexpected error'}), 500
        
        return jsonify({'result': 'OK', 'message': 'State updated successfully'}), 200

