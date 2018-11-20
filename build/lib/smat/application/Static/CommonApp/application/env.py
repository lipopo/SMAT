# -*- coding: utf8 -*-

# os工具
import os

"""
静态资源
"""

STATIC_PATH = os.path.join(os.path.dirname(__file__), "Static")

"""
动态共享资源
"""

"""
工具箱
"""

# 公用工具箱

# 本地工具箱


"""
应用初始化部分------------------------------------------------
"""
# 生成app handler
from .Tools.CommonTools.app import APP
# 初始化应用
app = APP()
# 注册模块的应用
from .Tools.CommonTools.register_app import register_module
# 导入模块
from Modules import *
# 导入主应用程式
import app as main_call

"""
------------------------------------------------------------
"""