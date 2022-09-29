from flask import request, current_app
from flask_restful import Resource
import json

class BaseView(Resource):
    @classmethod
    def get_sensor_list(self, sensor_type="all"):
        sensor_list_file = current_app.config.get("SENSOR_LIST_FILE", current_app.root_path+"/sensor_files/current_list.conf")
        sensor_list = {}
        with open(sensor_list_file, "r") as f:
            for line in f:
                sensor_description = json.loads(line)
                
                if sensor_type == "all":
                    sensor_list[sensor_description["name"]] = sensor_description["type"]

                elif sensor_description["type"] == sensor_type:
                    sensor_list[sensor_description["name"]] = sensor_description["type"]
     
        return sensor_list

    @classmethod
    def get_sensor_location(self, sensor_name):
        sensor_list_file = current_app.config.get("SENSOR_LIST_FILE", current_app.root_path+"/sensor_files/current_list.conf")
        with open(sensor_list_file, "r") as f:
            for line in f:
                sensor_description = json.loads(line)

                if sensor_description["name"] == sensor_name:     
                    return sensor_description["location"]