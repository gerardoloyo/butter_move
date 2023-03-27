from flask import Blueprint, request, jsonify
from api.validators import validators
from api.services.states_service import StatesService

states_controller = Blueprint('states_controller', __name__)

@states_controller.route('/state', methods=['POST'], endpoint='add_state')
@validators.validate_params(
    required_params={
        'abbreviation': (str, r'^[A-Z]{2}$'),
        'normal_commission': (float, None),
        'premium_commission': (float, None),
        'iva': (float, None),
        'base_discount': (dict, None),
        'total_discount': (dict, None),
        'premium_discount': (dict, None)
    }
)
def add_state():
    data = request.get_json()
    state_service = StatesService(
        abbreviation = data['abbreviation'],
        normal_commission = data['normal_commission'],
        premium_commission = data['premium_commission'],
        iva = data['iva'],
        base_discount = data['base_discount'],
        total_discount = data['total_discount'],
        premium_discount = data['premium_discount']
    )
    return state_service.add_state()


@states_controller.route('/state', methods=['PATCH'], endpoint='update_state')
@validators.validate_params(
    required_params={
        'abbreviation': (str, r'^[A-Z]{2}$'),
        'normal_commission': (float, None),
        'premium_commission': (float, None),
        'iva': (float, None),
        'base_discount': (dict, None),
        'total_discount': (dict, None),
        'premium_discount': (dict, None)
    }
)
def update_state():
    data = request.get_json()
    state_service = StatesService(
        abbrevation = data['abreviation'],
        normal_commission = data['normal_commission'],
        premium_commission = data['premium_commission'],
        iva = data['iva'],
        base_discount = data['base_discount'],
        total_discount = data['total_discount'],
        premium_discount = data['premium_discount']
    )
    return state_service.update_state()
