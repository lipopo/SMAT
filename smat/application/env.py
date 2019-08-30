# -*- coding: utf8 -*-

# os工具
import os


"""
静态目录
"""
# 静态资源目录
STATIC_PATH = os.path.join(os.path.dirname(__file__), "Static")
# json资源目录
JSON_PATH = os.path.join(STATIC_PATH, "jsons")

# 获取下载路径
smat_server_path = os.environ.get("SMAT_REMOTE_PATH", "http://www.robotli.cn/SMAT")

"""
工具箱
"""
# 公共工具箱
# 文件工具
import shutil
# sys工具
import sys
# json加载工具
import json

# 加载设置
load_json = json.load(open(os.path.join(JSON_PATH, "main.json"), "rb"))
accept_type = load_json["main"]["accept"]
translate_type = load_json["main"]["translate"]
# 本地工具
from .Modules.info import info

commands = []
command_list = {
}

"""
命令行工具组
"""
# help命令行
commands.append("help")
from .Modules.HelpCommand import HelpCommand
command_list["help"] = HelpCommand

# init命令行
commands.append("init")
from .Modules.InitCommand import InitCommand
command_list["init"] = InitCommand