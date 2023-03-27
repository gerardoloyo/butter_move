from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from api.controllers.estimations_controller import estimations_controller
    from api.controllers.states_controller import states_controller

    app.register_blueprint(estimations_controller)
    app.register_blueprint(states_controller)
    
    return app
