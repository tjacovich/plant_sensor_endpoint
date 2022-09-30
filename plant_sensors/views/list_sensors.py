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
            with open(self.get_sensor_file(), "a") as f:
                f.write("\n")
                json.dump(data, f)
                sensor_added = {"Added sensor": "{}".format(data)}
        except Exception as e:
            current_app.logger.error("Failed to add sensor with error: {}".format(e))
            sensor_added = {"error":"Failed to add sensor {}".format(data)}
        return sensor_added

    def get(self, sensor_type):
        response = self.get_sensor_list(sensor_type=sensor_type)
        if True:
            return response, 200
        
        else:
            return response, 500

    def post(self, sensor_type):
        data = request.get_json(force=True)
        response = self.add_sensor(data)
        if response:
            return response, 200
        
        else:
            return response, 400