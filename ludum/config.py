# -*- coding: utf-8 -*-
from os import environ

SECRET_KEY = environ.get('SECRET_KEY')
API_KEY = environ.get('API_KEY')

# DB Settings
SQLALCHEMY_TRACK_MODIFICATIONS = False

# SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://user:pass@localhost/db' # production db uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db' # development db uri
