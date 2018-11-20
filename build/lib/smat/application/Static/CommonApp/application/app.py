# -*- coding: utf8 -*-
from .env import register_module

# 注册main函数
@register_module("__call__")
def call():
    print "Call Me"