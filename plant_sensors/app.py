"""
Application
"""

import logging.config

from werkzeug.serving import run_simple
from .views import TemperatureView, HumidityView, MoistureView
from flask_restful import Api
from flask import request, Flask
from flask_discoverer import Discoverer

def create_app(**config):
    """
    Create the application and return it to the user
    :return: application
    """

    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_pyfile('../config.py')

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
                
    return app
       

if __name__ == '__main__':
    run_simple('0.0.0.0', 5000, create_app(), use_reloader=False, use_debugger=False)