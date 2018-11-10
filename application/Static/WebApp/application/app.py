# -*- coding: utf8 -*-

from .env import application
from .env import blueprint

def app():
    application.run("0.0.0.0", 8991, debug=True)