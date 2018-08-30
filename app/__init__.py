""" initialise the web server and present routes """

from flask_api import FlaskAPI
from instance.config import app_config

devices = [
    {
        'id': 1,
        'hostname': 'TestMachine',
        'notes': 'Owned by Mary'
    },
    {
        'id': 2,
        'hostname': 'TestMachine2',
        'notes': 'Owned by Joe'
    }
]

def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    return app