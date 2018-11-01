# -*- coding: utf8 -*-

# os工具
import os


"""
静态目录
"""
# 静态资源目录
STATIC_PATH = os.path.join(os.path.dirname(__file__), "Static")

"""
工具箱
"""
# 公共工具箱
# 文件工具
import shutil
# sys工具
import sys


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