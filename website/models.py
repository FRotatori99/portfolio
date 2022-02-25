from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

class Author(db.Model):
    __tablename__ = 'Author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    surname = db.Column(db.String(150))

class AuthorPhoto(db.Model):
    __tablename__ = 'AuthorPhoto'
    id = db.Column(db.Integer, primary_key=True)
    id_author = db.Column(db.Integer)

class QuoteCategory(db.Model):
    __tablename__ = 'QuoteCategory'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(150), unique=True)

class Quote(db.Model):
    __tablename__ = 'Quote'
    id = db.Column(db.Integer, primary_key=True)
    id_author = db.Column(db.Integer)
    id_category = db.Column(db.Integer)

class Language(db.Model):
    __tablename__ = 'Language'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(5)) # IT, EN
    description = db.Column(db.String(150)) # Italian, English

class Setting(db.Model):
    __tablename__ = 'Setting'
    id = db.Column(db.Integer, primary_key=True)
    id_default_language = db.Column(db.Integer)