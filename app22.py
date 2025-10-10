import os
import json
import logging.config
from flask import Flask, jsonify, request
from config22 import get_config 

config_name = os.environ.get('FLASK_CONFIG', 'development')
Config = get_config(config_name)

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    try:
        with open('logging_config22.json', 'rt') as f:
            log_config_dict = json.load(f)
        
        logger_name = f"flask_app_{config_object.LOG_PROFILE}"
        
        if logger_name in log_config_dict.get('loggers', {}):
         
            app.logger_name = logger_name 
            
  
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
    
            x = 1 / 0
        except ZeroDivisionError:
            app.logger.error("An ERROR occurred: division by zero!")
            app.logger.exception("CRITICAL error: Unrecoverable fault.")
        return "Error logged."
    
    return app

app = create_app(Config)

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])