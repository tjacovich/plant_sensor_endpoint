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
    def poll_sensors(self):
        sensor_list = {}
        return sensor_list
    
    @classmethod
    def add_sensor(self):
        sensor_added = {}
        return sensor_added

    def get(self, sensor_type):
        if True:
            return response, 200
        
        else:
            return response, 500

    def put(self, sensor_type):
        if True:
            return response, 200
        
        else:
            return response, 500