from flask import Blueprint, request, jsonify
from api.services import estimations_service

estimations_controller = Blueprint('estimations_controller', __name__)

@estimations_controller.route('/estimate', methods=['POST'])
def estimate():
    if not estimations_service.is_valid_ip(request.headers.get('ip-client')):
        return jsonify({'message': 'Invalid IP address'}), 400

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
