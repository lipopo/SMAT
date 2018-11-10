# -*- coding: utf8 -*-
from .env import app as app_module
from .env import main


# 注册main函数
app_module.register_module("main", main)


def call():
    print "Call Me"

app_module.register_module(
    "__call__" ,
    call
)