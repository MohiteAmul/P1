import  pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

from UTILITIES.BaseClass import BaseClass


class WebPage(BaseClass):

    def __init__(self,driver):
        self.driver=driver

    inpuBox_locator=(By.CSS_SELECTOR,'#myTextInput')


    def inputBox(self):
        return self.driver.find_element(*WebPage.inpuBox_locator)