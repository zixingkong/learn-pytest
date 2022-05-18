# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：   test_sysexit
   Description:  
   Date：        2022/5/18
-------------------------------------------------
"""
# content of test_sysexit.py
import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()
