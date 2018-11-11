# -*- coding: utf8 -*-
# os工具
import os
"""
静态资源
"""
# app名称
__appname__ = "SMAT_APP"
__urlprefix__ = "/SMAT"

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
from flask import Blueprint
"""
--------------------------------------------------
"""
# 本地工具箱

"""
应用构建
"""
"""
构建应用-------------------------------------------
"""
# 初始化应用

# 构建应用
app = Flask(__name__)
application = app
app.template_folder = TEMPLATE_PATH

# 构建蓝图
blueprint = Blueprint( name=__appname__, import_name=__name__, static_folder=STATIC_PATH, static_url_path=None, template_folder=TEMPLATE_PATH, url_prefix=__urlprefix__, subdomain=None, url_defaults=None, root_path=None)


# 主页
from .Modules.Index import Index

"""
---------------------------------------------------
"""