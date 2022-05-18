# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：   test_class_demo
   Description:  
   Date：        2022/5/18
-------------------------------------------------
"""


# content of test_class_demo.py
class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1
