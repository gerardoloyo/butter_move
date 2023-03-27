from flask import Blueprint, request
from api.validators import validators
from api.services.estimations_service import EstimationsService

estimations_controller = Blueprint('estimations_controller', __name__)

@estimations_controller.route('/estimate', methods=['POST'])
@validators.validate_params(
    required_params={
        'state': (str, r'^[A-Z]{2}$'),
        'estimation_type': (str, r'^(NORMAL|PREMIUM)$'),
        'kilometers': (float, None),
        'base_amount': (float, None)
    }
)
def estimate():
    data = request.get_json()
    estimations_service = EstimationsService(
        state = data['state'],
        estimation_type = data['estimation_type'],
        kilometers = data['kilometers'],
        base_amount = data['base_amount']
    )
    return estimations_service.calculate_estimation()
