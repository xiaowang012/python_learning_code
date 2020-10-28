#coding=utf-
#解决窗口无法定位元素的问题
#获取所有的窗口句柄，然后指定切换对应窗口
#使用unittest构建一个简单的测试用例，判断获取的文本是否一致
from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# driver=webdriver.Chrome()
# driver.maximize_window()

# driver.get('http://baidu.com')

# #搜索iphone
# ele=driver.find_element_by_id('kw')
# ele.clear()
# ele.send_keys('iphone')
# ele.submit()
# sleep(5)
# ele=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/h3/a')
# ele.click()
# #获取当前的所有窗口句柄（2个）
# handles=driver.window_handles
# print(handles)
# driver.switch_to_window(handles[-1])
# sleep(15)
# #点击iphone xr
# try:
#     ele=driver.find_element_by_xpath('/html/body/nav[2]/div/ul/li[4]/a')
# except:
#     print('Error')
# else:
#     ele.click()
   
# # #关闭当前窗口
# sleep(20)
# driver.quit()

# sleep(5)



class WebTest(unittest.TestCase):
    '''一个登录baidu.com的实例'''

    @classmethod
    def setUpClass(self):
        '''初始化，前置条件'''
        url='http://baidu.com'
        driver=webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get(url)
        self.driver=driver

    def test_1(self):
        driver=self.driver
        try:
            ele=driver.find_element_by_id('kw')
            ele.clear()
            ele.send_keys('iphone')
            ele.submit()
            sleep(5)
            ele=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/h3/a')
            ele.click()
        except:
            x=False
        else:
            x=True
        self.assertTrue(x,'没找到元素！')
    
    def test_2(self):
        driver=self.driver
        handles=driver.window_handles
        print(handles)
        driver.switch_to_window(handles[-1])
        sleep(15)
        try:
            ele=driver.find_element_by_xpath('/html/body/nav[2]/div/ul/li[4]/a')
        except:
            x=False
        else:
            x=True
            ele.click()
        self.assertTrue(x,'没找到元素！')
        
        a=ele.text
        print(a)
        self.assertEqual(a,'iPhone xR','元素不一致！！')
        
    
    @classmethod
    def tearDownClass(self):
        driver=self.driver
        driver.quit()


if __name__=='__main__':
    unittest.main()


