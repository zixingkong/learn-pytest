# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：   myinvoke
   Description:  
   Date：        2022/5/18
-------------------------------------------------
"""
# content of myinvoke.py
import pytest
import sys


class MyPlugin:
    def pytest_sessionfinish(self):
        print("*** test run reporting finishing")


if __name__ == "__main__":
    sys.exit(pytest.main(["-qq"], plugins=[MyPlugin()]))
