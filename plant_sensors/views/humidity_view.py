"""
Humidity view
"""

from flask import request, current_app, make_response, jsonify
from flask_restful import Resource
import requests

class HumidityView(Resource):


    def get():
        return 200