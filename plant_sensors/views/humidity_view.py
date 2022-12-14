"""
Humidity view
"""

from flask import request, current_app, make_response, jsonify
from flask_restful import Resource
import requests
import board
import adafruit_dht
from .base_view import BaseView
import sys
import time

class HumidityView(BaseView):
    @classmethod
    def init_connection(self, sensor_name="H0"):
        # Initial the dht device
        try:
            location = self.get_sensor_location(sensor_name)
            try:
                pin_name = getattr(sys.modules["board"], location)
            except:
                current_app.logger.warning("Could not get pin name. Assuming pin D4")
                pin_name = board.D4
        except:
            current_app.logger.error("Failed to set pin name. Stopping.")
            raise Exception

        return adafruit_dht.DHT11(pin_name)

    def get_humidity(self, dhtDevice):
        retries = current_app.config.get("N_RETRIES", 3)
        tries = 0
        while tries < retries:
            current_app.logger.info("Attempting to read humidity try: {}/{}".format(tries+1, retries))
            try:
                humidity = dhtDevice.humidity
                return {"humidity": humidity}

            except RuntimeError as error:
                # Errors happen fairly often, DHT's are hard to read, just keep going
                current_app.logger.error(error.args[0])
                time.sleep(2.0)
                tries +=1
                continue

            except Exception as error:
                current_app.logger.error(error.args[0])
                break
        
        current_app.logger.error("Failed to collect humidity from sensor")

        return {"error":"Failed to collect humidity from sensor"}

    def get(self):
        params = request.args.to_dict()
        dhtDevice = self.init_connection(sensor_name=params.get("name"))
        response = self.get_humidity(dhtDevice)
        dhtDevice.exit()
        
        if "error" not in response.keys():
            return response, 200
        
        else:
            return response, 500


