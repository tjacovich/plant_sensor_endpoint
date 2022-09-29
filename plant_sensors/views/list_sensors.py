import serial
import time
import json
from flask import request, current_app, make_response, jsonify
from flask_restful import Resource
import requests

class SensorsView(Resource):
    @classmethod
    def init_connection(self):
        sensor_list = {}
        return sensor_list
    
    @classmethod
    def poll_sensors(self, connection):

    
    def get(self, type):

            return response, 200
        
        else:
            return response, 500

