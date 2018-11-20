# -*- coding: utf8 -*-

from ..env import register_app
from ..env import render_template
#
@register_app("/", methods=["GET"])
def Index():
    def local_deal(func):
        content = func()
        return content

    @local_deal
    def main():
        return render_template("Index.html")

    return main