#!/usr/bin/env python3
#-*-coding:utf-8-*-

from flask import Flask

app = Flask(__name__)

def create_app(config):

    app.config.from_object(config)

from webapp import views
