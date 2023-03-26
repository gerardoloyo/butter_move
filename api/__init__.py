from flask import Flask
from config import Config
from api.controllers import estimations_controller

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(estimations_controller)

    return app
