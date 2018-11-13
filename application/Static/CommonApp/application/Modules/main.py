# -*- coding: utf8 -*-
from ..env import register_module

# 主应用函数
@register_module("main")
def main():
    print "a"
    return "a"