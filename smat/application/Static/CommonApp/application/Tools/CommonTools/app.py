# -*- coding: utf8 -*-

class APP(object):

    # 注册模块
    def register_module(self, module_name, module=None):
        # 设置自身变量
        object.__setattr__(self, module_name, module)
