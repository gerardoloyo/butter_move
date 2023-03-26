from flask import Blueprint, request, jsonify
from api.validators import validators
from api.models.states_model import State
from api import db

states_controller = Blueprint('states_controller', __name__)

@states_controller.route('/state', methods=['POST'])
@validators.validate_params(
    required_params={
        'abbreviation': (str, r'^[A-Z]{2}$'),
        'normal_commission': (float, None),
        'premium_commission': (float, None)
    }
)
def add_state():
    data = request.get_json()

    state = State(
        abbreviation=data['abbreviation'],
        normal_commission=data['normal_commission'],
        premium_commission=data['premium_commission']
    )

    db.session.add(state)
    db.session.commit()

    return jsonify({'message': 'State added successfully'}), 201

@states_controller.route('/state', methods=['PATCH'])
@validators.validate_params(
    required_params={
        'abbreviation': (str, r'^[A-Z]{2}$'),
        'normal_commission': (float, None),
        'premium_commission': (float, None)
    }
)
def update_state(abbreviation):
    data = request.get_json()
    state = State.query.filter_by(abbreviation).first()

    if not state:
        abort(404)

    state.normal_commission = data.get('normal_commission', state.normal_commission)
    state.premium_commission = data.get('premium_commission', state.premium_commission)

    db.session.commit()

    return jsonify({'message': 'State updated successfully'}), 200