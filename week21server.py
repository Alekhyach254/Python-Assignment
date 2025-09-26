from flask import Flask, request, jsonify
from cerberus import Validator
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

user_schema = {
    'email': {'type': 'string', 'required': True, 'empty': False, 'regex': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'}, # Checks basic email pattern
    'password': {'type': 'string', 'required': True, 'minlength': 6},
    'age': {'type': 'integer', 'required': True, 'min': 1, 'max': 150} 
}
user_validator = Validator(user_schema)

@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(500)
def handle_error(e):
   
    code = getattr(e, 'code', 500)
    
   
    message = getattr(e, 'description', 'An unexpected error occurred.')
    
   
    response = {
        'success': False,
        'status': code,
        'message': message
    }
    return jsonify(response), code


@app.route('/api/users/register', methods=['POST'])
def register_user():
    
    data = request.get_json()
    
    
    if data is None:
     
        return handle_error(BadRequest("Request body must be valid JSON.")), 400

  
    if not user_validator.validate(data):
       
        validation_errors = user_validator.errors
        
       
        error_messages = []
        for field, errors in validation_errors.items():
            error_messages.append(f"{field}: {', '.join(errors)}")
        
        
      
        response = {
            'success': False,
            'status': 400,
            'message': 'Input validation failed',
            'errors': validation_errors
        }
        return jsonify(response), 400

    
    
    
    return jsonify({
        'success': True,
        'message': 'User registered successfully',
        'user': data
    }), 201

if __name__ == '__main__':
    
    app.run(debug=True)