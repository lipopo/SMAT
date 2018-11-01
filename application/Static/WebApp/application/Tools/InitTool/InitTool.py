# -*- coding: utf8 -*-
"""
初始化项目
"""
from ...env import LIB_PATH
from ...env import os
from ...env import file_dict, files

from .FildFiles import FindFiles
def InitTool():
    pathes = FindFiles(LIB_PATH)
    for path in pathes:
        file_name = os.path.split(path)[1]
        files.append(file_name)
        file_dict[file_name] = {}
        file_dict[file_name]["content"] = open(path, "rb").read()
        file_dict[file_name]["filetype"] = file_name.split(".")[-1]