#-*- coding: utf8 -*-

from setuptools import setup, find_packages


version = "0.0.1"

install_packages = [

]

setup(
    name="smat",
    author="lipo",
    author_email="15510520668@163.com",
    maintainer="lipo",
    maintainer_email="15510520668@163.com",
    packages=find_packages(),
    include_package_data=True,
    install_packages=install_packages,
    description="A Quick Scaffold",
    platforms="any",
    entry_points={
        "console_scripts": [
            "smat = smat.smat:app"
        ]
    }
)