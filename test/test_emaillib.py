# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：   test_emaillib
   Description:  
   Date：        2022/5/18
-------------------------------------------------
"""
# content of test_emaillib.py
# import pytest
#
# from lib.emaillib import Email, MailAdminClient
#
#
# @pytest.fixture
# def mail_admin():
#     return MailAdminClient()
#
#
# @pytest.fixture
# def sending_user(mail_admin):
#     user = mail_admin.create_user()
#     yield user
#     mail_admin.delete_user(user)
#
#
# @pytest.fixture
# def receiving_user(mail_admin):
#     user = mail_admin.create_user()
#     yield user
#     mail_admin.delete_user(user)
#
#
# def test_email_received(sending_user, receiving_user):
#     email = Email(subject="Hey!", body="How's it going?")
#     sending_user.send_email(email, receiving_user)
#     assert email in receiving_user.inbox


# content of test_emaillib.py
import pytest

from lib.emaillib import Email, MailAdminClient


@pytest.fixture
def mail_admin():
    return MailAdminClient()


@pytest.fixture
def sending_user(mail_admin):
    user = mail_admin.create_user()
    yield user
    mail_admin.delete_user(user)


@pytest.fixture
def receiving_user(mail_admin, request):
    user = mail_admin.create_user()

    def delete_user():
        mail_admin.delete_user(user)

    request.addfinalizer(delete_user)
    return user


@pytest.fixture
def email(sending_user, receiving_user, request):
    _email = Email(subject="Hey!", body="How's it going?")
    sending_user.send_email(_email, receiving_user)

    def empty_mailbox():
        receiving_user.clear_mailbox()

    request.addfinalizer(empty_mailbox)
    return _email


def test_email_received(receiving_user, email):
    assert email in receiving_user.inbox
