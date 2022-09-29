import serial
import time
import json
from flask import request, current_app, make_response, jsonify
from flask_restful import Resource
from .base_view import BaseView
import requests

class MoistureView(BaseView):
    @classmethod
    def init_connection(self, sensor_name="M0"):
        # open a serial connection
        current_app.logger.info("Initializing connection to Pico")
        try:
            device_location = self.get_sensor_location(sensor_name)
        except:
            current_app.logger.warning("Failed to get sensor data from sensors file. Falling back to config file.")
            device_location = current_app.config.get("DEVICE_LOCATION", "/dev/ttyACM0")
        s = serial.Serial(device_location, 115200)
        s.timeout = 3
        return s
    
    @classmethod
    def poll_sensor(self, connection):
        current_app.logger.info("Sending command to device")
        connection.write(b"take reading\n")
        readings = connection.readline().strip().split()
        try:
            readings_json = {"moisture content": float(readings[0]), "raw": int(readings[1])}
        except Exception as e:
            current_app.logger.error('Failed to retrieve reading from Moisture Sensor with error {}'.format(e))
            readings_json = {"error":"Failed to retrieve reading from Moisture Sensor"}
        return readings_json
    
    def get(self):
        connection = self.init_connection()
        response = self.poll_sensor(connection)

        if "error" not in response.keys():
            return response, 200
        
        else:
            return response, 500

