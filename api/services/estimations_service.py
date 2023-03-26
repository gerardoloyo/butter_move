from datetime import datetime
from typing import Dict
from api.models.states_model import State

STATE_COMMISSIONS = {
    'NY': {'NORMAL': 0.25, 'PREMIUM': 0.35},
    'CA': {'NORMAL': 0.23, 'PREMIUM': 0.33},
    'AZ': {'NORMAL': 0.20, 'PREMIUM': 0.30},
    'TX': {'NORMAL': 0.18, 'PREMIUM': 0.28},
    'OH': {'NORMAL': 0.15, 'PREMIUM': 0.25}
}

def calculate_estimation(state: str, estimation_type: str, kilometers: float, base_amount: float) -> Dict[str, str]:
    state = state.upper()
    estimation_type = estimation_type.upper()
    state_obj = State.query.filter_by(abbreviation=state).first()
    
    if not state_obj:
        raise ValueError('Unsupported state')

    commission = state_obj.normal_commission if estimation_type == 'NORMAL' else state_obj.premium_commission
    total_amount = base_amount * (1 + commission)

    if estimation_type == 'NORMAL':
        if state == 'NY':
            total_amount *= 1.21
        elif state in ('CA', 'AZ') and kilometers > 26:
            total_amount *= 0.95
        elif state in ('TX', 'OH'):
            if 20 <= kilometers <= 30:
                total_amount *= 0.97
            elif kilometers > 30:
                total_amount *= 0.95
    elif estimation_type == 'PREMIUM':
        if kilometers > 25:
            total_amount *= 0.95

    return {
        'total_amount': round(total_amount, 2),
        'processed_date': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    }


