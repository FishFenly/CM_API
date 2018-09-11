""" run development server """
import os
from app import create_app

# create the flask object by calling the create app function with the right config
config_name = 'development'
app = create_app(config_name)

# run the flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)