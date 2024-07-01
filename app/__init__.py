from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()

def create_app():
    '''function to create and configure the Flask application'''

    app = Flask(__name__)
    app.config.from_object('app.config.Config')     # Loads configuration settings from the Config class in config.py.
    mongo.init_app(app)

    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
