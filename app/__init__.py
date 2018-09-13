""" initialise the web server and define routes """

from flask import Flask, request, render_template, jsonify
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
    
    # route for getting a single device
    @app.route('/v1.0/devices', methods=['POST'])
    def get_device():
        cn = request.args['name']
        device = str(get(cn))
        return jsonify(device), 200

    # route for posting devices
    @app.route('/v1.0/devices', methods=['POST'])
    def add_device():
        """ function runs when URI is accessed """
        post(request.args['name'],request.args['mac'])
        return '', 201

    return app