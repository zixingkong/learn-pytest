# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：   test_class
   Description:  
   Date：        2022/5/18
-------------------------------------------------
"""


# content of test_class.py
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
