""" initialise the web server and present routes """

from flask import Flask, request
from instance.config import app_config
from models import Devices

def create_app(config_name):
    """ function creates the flask app using the config file """
    # intialise flask app
    app = Flask(__name__)
    # load the configuration
    app.config.from_object(app_config[config_name])

    # route for getting devices
    @app.route('/v1.0/devices')
    def get_alldevices():
        devices = Devices()
        devices.getall()
        return devices
    
    @app.route('/v1.0/devices/test')
    def get_device():
        device = Devices()
        device.get('NG0392')
        return device

    # route for posting devices
    @app.route('/v1.0/devices', methods=['POST'])
    def add_device():
        """ function runs when URI is accessed """
        device = Devices()
        device.post(str(request.data.get('name')),)
        return '', 204

    return app