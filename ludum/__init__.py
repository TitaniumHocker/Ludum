# -*- coding: utf-8 -*-
from .app import app as application
from .extensions import db
from .models import *
from . import views


def get_app():
    return application
