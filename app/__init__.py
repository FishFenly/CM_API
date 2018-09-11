""" initialise the web server and define routes """

from flask import Flask, request, render_template
from instance.config import app_config
from .models import get, getall, post

def create_app(config_name):
    """ function creates the flask app using the config file """
    # intialise flask app
    app = Flask(__name__)
    # load the configuration
    app.config.from_object(app_config[config_name])

    # handle 404 errors using custom html
    @app.errorhandler(404)
    def handle_notfound(e):
        return render_template('404.html'), 404

    # route for getting devices
    @app.route('/v1.0/devices')
    def get_alldevices():
        devices = getall()
        return devices, 200
    
    @app.route('/v1.0/devices/test')
    def get_device():
        device = get('NG0392')
        return device, 200

    # route for posting devices
    @app.route('/v1.0/devices', methods=['POST'])
    def add_device():
        """ function runs when URI is accessed """
        post(str(request.data.get('name')),str(request.data.get('mac')))
        return '', 201

    return app