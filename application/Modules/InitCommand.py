# -*- coding: utf8 -*-
"""
初始化命令
"""
from ..env import STATIC_PATH
from ..env import os, shutil

def InitCommand(args):
    info = """
smat init --<参数>=<参数值> --<参数>=<参数值> <应用名称>
支持的参数
    type ---- 创建的应用类型，目前支持[command_app, web_app] 默认类型为web_app
"""

    accept_key = ["type"]
    accept_type = ["web_app", "command_app", "dock_app", "common_app"]
    template_dict = {
        "web_app": "WebApp",
        "command_app": "CommandApp",
        "dock_app": "DockApp",
        "common_app": "CommonApp"
    }
    if len(args) == 0 or args[0] == "help" or args[-1].find("--") >= 0:
        print(info)
        return
    else:
        app_name = args[-1]
        app_type = "web_app"
        val_arg = [tuple(arg.replace("--", "").split("=")) for arg in list(filter(lambda arg: arg[:2] == "--",args))]

        for k, v in val_arg:
            if k == "type":
                if v in accept_type:
                    app_type = v
                else:
                    print(info)
                    return
            else:
                print(info)

        src_path = os.path.join(STATIC_PATH, template_dict[app_type])
        # print(src_path)
        if os.path.exists(app_name):
            print("此项目已经存在...")
            return None
        # os.mkdir(app_name)
        shutil.copytree(src_path, app_name)

