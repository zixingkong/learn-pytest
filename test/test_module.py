# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：   test_module
   Description:  
   Date：        2022/5/18
-------------------------------------------------
"""

# content of test_module.py


def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert b"smtp.gmail.com" in msg
    assert 0  # for demo purposes


def test_noop(smtp_connection):
    response, msg = smtp_connection.noop()
    assert response == 250
    assert 0  # for demo purposes
