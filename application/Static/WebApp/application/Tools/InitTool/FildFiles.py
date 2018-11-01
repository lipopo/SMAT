# -*- coding: utf8 -*-

from ...env import os

def FindFiles(path):
    flist = [os.path.join(path, fname) for fname in os.listdir(path)]
    paths = list(filter(lambda fpath: not os.path.isdir(fpath),flist))
    dir_list = list(filter(lambda fpath: os.path.isdir(fpath),flist))
    for dir in dir_list:
        paths.extend(FindFiles(dir))
    return paths
