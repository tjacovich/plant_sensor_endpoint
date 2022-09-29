from flask import request, current_app
from flask_restful import Resource


class BaseView(Resource):
    @classmethod
    def get_sensor_list(self):
        sensor_list_file = current_app.config.get("SENSOR_LIST_FILE", "../sensor_files/current_list.conf")
        with open(sensor_list_file, "r") as f:
            sensor_list = {lst[0]: lst[1] for lst in f.readline().split('\t')}
        return sensor_list