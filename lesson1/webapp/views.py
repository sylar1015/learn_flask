#!/usr/bin/env python3
#-*-coding:utf-8-*-

from webapp import app

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return 'Hello Flask!'


