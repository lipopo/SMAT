# -*- coding: utf8 -*-

from ...env import app

def register_module(module_name):

    def main(func):
        app.register_module(module_name, func)

    return main