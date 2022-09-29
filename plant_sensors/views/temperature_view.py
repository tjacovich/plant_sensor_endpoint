"""
Temperature view
"""

from flask import request, current_app, make_response, jsonify
from flask_restful import Resource
import requests
import board
import adafruit_dht
import time

class TemperatureView(BaseView):
    @classmethod
    def init_connection(self, sensor_name="T0"):
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

    def get_temperature(self, dhtDevice, celsius=True):
        retries = current_app.config.get("N_RETRIES", 3)
        tries = 0
        while tries < retries:
            current_app.logger.info("Attempting to read temperature try: {}/{}".format(tries+1, retries))
            try:
                if celsius: 
                    temperature = dhtDevice.temperature
                else:
                    temperature = dhtDevice.temperature * (9 / 5) + 32
                return {"temperature": temperature}

            except RuntimeError as error:
                # Errors happen fairly often, DHT's are hard to read, just keep going
                current_app.logger.error(error.args[0])
                time.sleep(2.0)
                tries +=1
                continue

            except Exception as error:
                current_app.logger.error(error.args[0])
                break
        
        current_app.logger.error("Failed to collect Temperature from sensor")

        return {"error":"Failed Collect Temperature from sensor"}

    def get(self):
        params = request.args.to_dict()
        dhtDevice = self.init_connection(sensor_name=params.get("name"))        
        response = self.get_temperature(dhtDevice)
        dhtDevice.exit()
        
        if "error" not in response.keys():
            return response, 200
        
        else:
            return response, 500



