"""
Temperature view
"""

from flask import request, current_app, make_response, jsonify
from flask_restful import Resource
import requests
import board
import adafruit_dht

class TemperatureView(Resource):
    @classmethod
    def init_connection(self, pin=board.D4):
        # Initial the dht device, with data pin connected to:
        return adafruit_dht.DHT11(pin)

    def get_temperature(self, dhtDevice, celsius=True):
        retries=current_app.logger.config.get("N_RETRIES", 3)

        while tries <= retries:
            try:
                if celsius: 
                    temperature_c = dhtDevice.temperature
                else:
                    temperature = dhtDevice.temperature * (9 / 5) + 32
                return {"temperature": temperature}

            except RuntimeError as error:
                # Errors happen fairly often, DHT's are hard to read, just keep going
                current_app.logger.error(error.args[0])
                time.sleep(2.0)
                continue

            except Exception as error:
                break
        
        current_app.logger.error("Failed Collect Temperature from sensor")

        return {"error":"Failed Collect Temperature from sensor"}, 500

    def get():
        dhtDevice = self.init_connection()
        response = self.get_temperature(dhtDevice)
        dhtDevice.exit()
        
        if "error" not in response.keys():
            return response, 200
        
        else:
            return respons, 500



