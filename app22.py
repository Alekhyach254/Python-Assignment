import os
import json
import logging.config
from flask import Flask, jsonify, request
# --- CHANGE 1: Use config22 ---
from config22 import get_config 

# --- 1. Load Configuration ---
config_name = os.environ.get('FLASK_CONFIG', 'development')
Config = get_config(config_name)

# --- 2. Setup Flask App and Logging ---
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    # 2a. Configure Python Logging
    try:
        # --- CHANGE 2: Use logging_config22.json ---
        with open('logging_config22.json', 'rt') as f:
            log_config_dict = json.load(f)
        
        logger_name = f"flask_app_{config_object.LOG_PROFILE}"
        
        if logger_name in log_config_dict.get('loggers', {}):
            # Set Flask's logger name to match the one in the config file
            app.logger_name = logger_name 
            
            # Apply the full logging dictionary configuration
            logging.config.dictConfig(log_config_dict)
            app.logger.info(f'Logging configured using profile: {config_object.LOG_PROFILE}')
        else:
            logging.basicConfig(level=logging.INFO)
            app.logger.warning('Could not find specific logger config, using basic config.')

    except FileNotFoundError:
        logging.basicConfig(level=logging.INFO)
        app.logger.error("logging_config22.json not found! Check your path.")
    except Exception as e:
        app.logger.error(f"Error configuring logging: {e}")

    # --- 3. Define Routes with Different Log Levels ---
    @app.route('/')
    def index():
        app.logger.info(f"Route '/' accessed.")
        return "Check your logs (console for dev, app.log for prod)."

    @app.route('/test/warning')
    def warning_route():
        app.logger.warning("A warning condition encountered on /test/warning route.")
        return "Warning logged."

    @app.route('/test/error')
    def error_route():
        try:
            # Simulate a failure
            x = 1 / 0
        except ZeroDivisionError:
            app.logger.error("An ERROR occurred: division by zero!")
            app.logger.exception("CRITICAL error: Unrecoverable fault.")
        return "Error logged."
    
    return app

# --- 4. Initialize the application instance that Flask looks for ---
app = create_app(Config)

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])