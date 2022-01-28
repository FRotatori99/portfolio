import imp
from sys import prefix
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "qwerty123"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, prefix="/")
    app.register_blueprint(auth, prefix="/")

    return app