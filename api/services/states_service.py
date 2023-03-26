from flask import jsonify
from api.models.states_model import State
from api import db

class StatesService:
    def __init__(self, abbrevation, normal_commission, premium_commission):
        self.abbreviation = abbrevation
        self.normal_comission = normal_commission
        self.premium_comission = premium_commission
    

    def add_state(self):
        try:
            state = State(
                abbreviation = self.abbreviation,
                normal_comission = self.normal_comission,
                premium_comission = self.premium_comission 
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

            normal_com = current_state.normal_comission if self.normal_comission is None else self.normal_commission
            premium_com = current_state.premium_comission if self.premium_comission is None else self.premium_comission
            current_state.normal_commission = normal_com
            current_state.premium_commission = premium_com

            db.session.commit()
        except Exception as e:
            return jsonify({'result': 'ERROR', 'message': 'Unexpected error'}), 500
        
        return jsonify({'result': 'OK', 'message': 'State updated successfully'}), 200

