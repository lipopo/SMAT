# -*- coding: utf8 -*-

from .env import sys
from .env import info, command_list

def app():
    # smat <command> <args...>
    args = sys.argv
    if len(args) == 1:
        # 输出信息
        print(info)
    else:
        command_list[args[1]](args[2:])


