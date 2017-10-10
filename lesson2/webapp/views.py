#!/usr/bin/env python3
#-*-coding:utf-8-*-

from webapp import app
from flask import render_template

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return '<body>Hello Flask!</body>'


