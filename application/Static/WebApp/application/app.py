# -*- coding: utf8 -*-

from .env import application

def app():
    application.run("0.0.0.0", 8991, debug=True)