# -*- coding: utf-8 -*-
from flask import (
        render_template,
        url_for, abort,
        redirect, request)
from .app import app
from .extensions import db
from .models import *


@app.route('/')
def index_page():
    return render_template('index.html')

