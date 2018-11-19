# -*- coding: utf8 -*-

from ...env import app, blueprint

def register_app(rule, **options):

    def decorator(f):
        endpoint = options.pop("endpoint", None)
        app.add_url_rule(rule, endpoint,view_func=f, **options)
        blueprint.add_url_rule(rule, endpoint,view_func=f, **options)
        return f

    return decorator