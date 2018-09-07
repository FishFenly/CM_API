""" initialise the web server and present routes """

from flask import Flask
from instance.config import app_config
from models import Devices

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    @app.route('/v1.0/devices', methods=['POST', 'GET'])
    def devices():
        device = Devices()
        if request.method == 'POST':
            # POST
            device.post(str(request.data.get('name'))
        else:
            # GET
            device.get(str)
    return app