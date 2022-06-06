import time
import unittest

from selenium import webdriver

from pageobject.login_page import LoginPage


class TestCase(unittest.TestCase):

    def test_01_login(self):
        lp = LoginPage()
        lp.login_pc()
