from flask import request, jsonify
import re

def validate_params(required_params):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Check ip-client header
            if not is_valid_ip(request.headers.get('ip-client')):
                return jsonify({'status': 'FAIL', 'message': 'Invalid IP address'}), 400
            
            data = request.get_json(silent=True)

            # Check if there is json on request
            if not data:
                return jsonify({'status': 'FAIL', 'message': 'Missing JSON in request'})

            # Check for missing parameters
            missing_params = [param for param in required_params if param not in data]
            if missing_params:
                return jsonify({'status': 'FAIL', 'message': 'Missing required parameters'}), 400

            # Check each parameter to be of the correct type and pattern
            incorrect_types_or_patterns = [
                param for param, (expected_type, regex_pattern) in required_params.items()
                if not isinstance(data[param], expected_type) or (isinstance(data[param], str) and regex_pattern and not re.match(regex_pattern, data[param].upper()))
            ]
            if incorrect_types_or_patterns:
                return jsonify({'status': 'FAIL', 'message': 'Incorrect parameter types or patterns'}), 400
            
            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator


def is_valid_ip(ip: str) -> bool:
    ipv4_pattern = re.compile(
        r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    )
    ipv6_pattern = re.compile(
        r'^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|(::[0-9a-fA-F]{1,4}){1,7}|[0-9a-fA-F]{1,4}::{1,7}|[0-9a-fA-F]{1,4}::[0-9a-fA-F]{1,4}(:[0-9a-fA-F]{1,4}){1,5})$'
    )

    return bool(ipv4_pattern.match(ip) or ipv6_pattern.match(ip))
