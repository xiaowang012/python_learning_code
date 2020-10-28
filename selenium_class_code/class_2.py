import unittest
from selenium import webdriver

#单元测试框架unittest 的TestCase类，该代通过继承TestCase类然后添加一个测试方法。（class_1.py中的代码）
#setUp()方法用来初始化程序，

class SearchTest(unittest.TestCase):
    '''继承TestCase类'''
    def setUp(self):
        '''初始化配置'''
        #创建一个火狐浏览器实例
        self.driver=webdriver.firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        #get主页
        self.driver.get('http://www.baidu.com')

    def test_search_by_category(self):
        #查找搜索框
        self.search_field=self.driver.find_element_by_name('q')
        self.search_field.clear()

        #发送指定字符
        self.search_field.send_keys('phones')
        self.search_field.submit()

        

#在火狐浏览器的默认界面搜索框输入'iphone'
# driver=webdriver.firefox()
# driver.maximize_window()

# driver.get(r'https://home.firefoxchina.cn/') #search-key
# ele=driver.find_element_by_name('search-key')
# ele.send_keys('iphone')



