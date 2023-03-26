from flask import Blueprint, request, jsonify
from api.validators import validators
from api.services import estimations_service

estimations_controller = Blueprint('estimations_controller', __name__)

@estimations_controller.route('/estimate', methods=['POST'])
@validators.validate_params(
    required_params={
        'state': str,
        'estimation_type': str,
        'kilometers': float,
        'base_amount': float
    }
)
def estimate():
    data = request.get_json()

    try:
        result = estimations_service.calculate_estimation(
            data['state'],
            data['estimation_type'],
            data['kilometers'],
            data['base_amount']
        )
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

    return jsonify(result), 200
