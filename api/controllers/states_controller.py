from flask import Blueprint, request, jsonify
from api.validators import validators
from api.services.states_service import StatesService

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
    state_service = StatesService(
        abbreviation = data['abbreviation'],
        normal_commission = data['normal_commission'],
        premium_commission = data['premium_commission']
    )
    return state_service.add_state()


@states_controller.route('/state', methods=['PATCH'])
@validators.validate_params(
    required_params={
        'abbreviation': (str, r'^[A-Z]{2}$'),
        'normal_commission': (float, None),
        'premium_commission': (float, None)
    }
)
def update_state():
    data = request.get_json()
    state_service = StatesService(
        abbrevation = data['abreviation'],
        normal_commission = data['normal_comission'],
        premium_commission = data['premium_comission']
    )
    return state_service.update_state()
