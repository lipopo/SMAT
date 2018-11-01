# -*- coding: utf8 -*-
# os工具
import os
"""
静态资源
"""
# 静态文件夹路径
STATIC_PATH = os.path.join(os.path.dirname(__file__), "Static")
# 模板文件夹路径
TEMPLATE_PATH = os.path.join(STATIC_PATH, "Template")
# 资源文件夹路径
ASSETS_PATH = os.path.join(STATIC_PATH, "Assets")
# 资源库文件夹
LIB_PATH = os.path.join(STATIC_PATH, "Lib")

"""
动态资源组
"""
# 文件字典
file_dict = {}
# 文件数组
files = []

"""
工具箱
"""
# 公共工具箱
"""
flask工具组----------------------------------------
"""
from flask import Flask
from flask import render_template
from flask import request
from flask import Response
"""
--------------------------------------------------
"""
# 本地工具箱
from .Tools.InitTool.InitTool import InitTool
"""
应用构建
"""
"""
构建应用-------------------------------------------
"""
# 初始化应用
InitTool()

# 构建应用
app = Flask(__name__)
application = app
app.template_folder = TEMPLATE_PATH

# 主页
from .Modules.Index import Index

# 静态资源页面
from .Modules.Static import Static
"""
---------------------------------------------------
"""