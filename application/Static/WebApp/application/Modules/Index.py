# -*- coding: utf8 -*-

from ..env import app
from ..env import render_template

@app.route("/", methods=["GET"])
def Index():
    def local_deal(func):
        content = func()
        return content

    @local_deal
    def main():
        return render_template("Index.html")

    return main