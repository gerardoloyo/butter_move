from datetime import datetime
import re
from typing import Dict

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

    if state not in STATE_COMMISSIONS:
        raise ValueError('Unsupported state')

    commission = STATE_COMMISSIONS[state][estimation_type]
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


def is_valid_ip(ip: str) -> bool:
    ipv4_pattern = re.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    ipv6_pattern = re.compile(r'^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|(::[0-9a-fA-F]{1,4}){1,7}|[0-9a-fA-F]{1,4}::{1,7}|[0-9a-fA-F]{1,4}::[0-9a-fA-F]{1,4}(:[0-9a-fA-F]{1,4}){1,5})$')

    return bool(ipv4_pattern.match(ip) or ipv6_pattern.match(ip))

