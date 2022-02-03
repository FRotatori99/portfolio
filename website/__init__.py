from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database, drop_database
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
USER = "root"
PSW = "root"
HOST = "127.0.0.1"
DB_NAME = "website"
DATABASE_URI = "mysql+pymysql://{user}:{pw}@{host}/{db}".format(user=USER, pw=PSW, host=HOST, db=DB_NAME)

def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config["SECRET_KEY"] = "qwerty123"
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    from .views import views
    from .auth import auth 

    app.register_blueprint(views, prefix="/")
    app.register_blueprint(auth, prefix="/")

    from .models import User

    init_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login" # Se richiedono pagine che necessitano il login vengono reindirizzati al login
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def init_database(app):
    if not database_exists(DATABASE_URI):
        create_database(DATABASE_URI)
        db.create_all(app=app)
        print("Created Database")