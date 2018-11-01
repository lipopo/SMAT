# -*- coding: utf8 -*-

from ..env import app
from ..env import Response
from ..env import files, file_dict
@app.route("/static/<file_name>", methods=["GET"])
def Static(file_name):
    if file_name not in files:
        return ""
    content = file_dict[file_name]["content"]
    ftype = file_dict[file_name]["filetype"]

    def local_deal(func):
        response = func()
        if ftype == "css":
            response.headers["content-type"] = "text/css"
        return response

    @local_deal
    def main():
        response = Response(content)
        return response

    return main