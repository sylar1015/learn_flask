#!/usr/bin/env python3
#-*-coding:utf-8-*-


class DevConfig:

    DEBUG = True
    SECRET_KEY = '123456'

config = {

    'dev': DevConfig,
    'default' : DevConfig,
}
