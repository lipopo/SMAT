# -*- coding: utf8 -*-
from ..env import info, commands, command_list

def HelpCommand(args):
    if len(args) == 0:
        print(info)
    else:
        if args[0] not in commands:
            print(info)
        else:
            command_list[args[0]](["help"])
