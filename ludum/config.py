# -*- coding: utf-8 -*-
from os import environ, path

SECRET_KEY = environ.get('SECRET_KEY')
API_KEY = environ.get('API_KEY')
SECURITY_PASSWORD_SALT = environ.get('SECURITY_PASSWORD_SALT') 
SECURITY_PASSWORD_HASH = environ.get('SECURITY_PASSWORD_HASH')

# DB Settings
SQLALCHEMY_TRACK_MODIFICATIONS = False


# SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://user:pass@localhost/db' # production db uri
# SQLALCHEMY_DATABASE_URI = 'sqlite:///../dev.db' # development db uri
SQLALCHEMY_DATABASE_URI = f'sqlite:///{path.join(path.dirname(__file__), path.pardir, "db.sqlite")}'
