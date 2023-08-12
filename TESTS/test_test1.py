import time

import pytest
from selenium.webdriver.common.by import By

from PAGEOBJECTS.WebPage import WebPage
from UTILITIES.BaseClass import BaseClass
from TESTDATA.HomePageData import HomePageData


class TestOne(BaseClass):

    def test_e2e(self,getData):
        log = self.getLogger()
        webpage=WebPage(self.driver)
        log.info("this is amulmohite")
        webpage.inputBox().send_keys(getData["FNAME"])
        time.sleep(10)

    @pytest.fixture(params=HomePageData.getTestdata('T1'))
    def getData(self,request):
        return request.param

    def test_e1e():
        print("hello ")

    def test_p1():
        print("hello2")

    def test_p2():
        print('hello3')