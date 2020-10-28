# coding=utf-8
from selenium import webdriver
import unittest, time

class SwitchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30) #隐式等待时间为30秒
        self.base_url = "https://www.baidu.com"
    
    def test_baidu(self):
       '''aaa'''

    def tearDown(self):
        self.driver.quit()




if __name__ == "__main__":
    unittest.main()


