#!/usr/bin/env python3
#-*-coding:utf-8-*-

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
debug_toolbar = DebugToolbarExtension()

def create_app(config):

    app.config.from_object(config)
    debug_toolbar.init_app(app)

from webapp import views
