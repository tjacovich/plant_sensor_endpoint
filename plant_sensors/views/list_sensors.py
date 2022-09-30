import serial
import time
import json
from flask import request, current_app, make_response, jsonify
from flask_restful import Resource
from .base_view import BaseView
import requests

class SensorsView(BaseView):
    @classmethod
    def init_connection(self):
        sensor_list = {}
        return sensor_list
    
    @classmethod
    def poll_sensors(self):
        sensor_list = {}
        return sensor_list
    
    @classmethod
    def add_sensor(self, data):
        sensor_added = {}
        try:
            with open(self.sensor_list_file, "a") as f:
                line = json.dumps(data)
                f.write(line)
                sensor_added = {"Added sensor: {}".format(line)}
        except Exception as e:
            logger.error("Failed to add sensor with error: {}".format(e))
            sensor_added = {"error":"Failed to add sensor {}".format(line)}
        return sensor_added

    def get(self, sensor_type):
        response = self.get_sensor_list(sensor_type=sensor_type)
        if True:
            return response, 200
        
        else:
            return response, 500

    def post(self):
        data = request.get_json(force=True)
        response = self.add_sensor(data)
        if response:
            return response, 200
        
        else:
            return response, 400