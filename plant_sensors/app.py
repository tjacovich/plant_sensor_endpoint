"""
Application
"""

import logging.config

from werkzeug.serving import run_simple
from .views import TemperatureView, HumidityView, MoistureView, SensorsView
from flask_restful import Api
from flask import request, Flask
from flask_discoverer import Discoverer

log_level = {'DEBUG': logging.DEBUG, 
                  'INFO': logging.INFO,
                  'WARNING': logging.WARNING,
                  'ERROR': logging.ERROR,
                 }

def create_app(**config):
    """
    Create the application and return it to the user
    :return: application
    """

    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_pyfile('../config.py')
    log_set = app.config.get('LOGGING_LEVEL', 'INFO')
    app.logger.setLevel(log_level[log_set])

    # Register extensions
    api = Api(app)
    Discoverer(app)
    
    # Add the end resource end points
    api.add_resource(TemperatureView,
                     '/sensors/temperature',
                     methods=['GET'])

    api.add_resource(HumidityView,
                     '/sensors/humidity',
                     methods=['GET'])

    api.add_resource(MoistureView,
                     '/sensors/moisture',
                     methods=['GET'])
    
    api.add_resource(SensorsView,
                    '/sensors/available/<string:sensor_type>',
                    methods=['GET','PUT'])
                
    return app
       

if __name__ == '__main__':
    run_simple('0.0.0.0', 5000, create_app(), use_reloader=False, use_debugger=False)