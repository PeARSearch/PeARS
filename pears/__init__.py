#!/usr/bin/env python

from flask import Flask, Blueprint
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from pears import models

from pears.views import main
from pears.views import api

app.register_blueprint(main.mod)
app.register_blueprint(api.mod)
