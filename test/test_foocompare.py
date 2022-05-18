# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：   test_foocompare
   Description:  
   Date：        2022/5/18
-------------------------------------------------
"""


# content of test_foocompare.py
class Foo:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val


def test_compare():
    f1 = Foo(1)
    f2 = Foo(2)
    assert f1 == f2
