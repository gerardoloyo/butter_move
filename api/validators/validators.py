from flask import request, jsonify

def validate_params(required_params):
    def decorator(func):
        def wrapper(*args, **kwargs):
            data = request.get_json()

            # Check if there is json on request
            if not data:
                return jsonify({"message": "Missing JSON in request"}), 400

            # Check for missing parameters
            missing_params = [param for param in required_params if param not in data]
            if missing_params:
                return jsonify({"message": "Missing required parameters"}), 400

            # Check each parameter to be of the correct type
            incorrect_types = [
                param for param, expected_type in required_params.items()
                if not isinstance(data[param], expected_type)
            ]
            if incorrect_types:
                return jsonify({"message": "Incorrect parameter types"}), 400
            
            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator
