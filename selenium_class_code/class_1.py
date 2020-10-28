#selenium 自动化基础
#
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


browser=webdriver.Firefox()
browser.maximize_window()
url_1='http:\\www.baidu.com'
url_2=r'https://home.firefoxchina.cn/'
url_3=r'https://www.feisu.com/'#CityAjax
# browser.get(url_2)
# print(browser.page_source)
# browser.close()

#打印网页标题,title后面不能加括号否则报TypeError：'str' object is not callable
# wangye=browser.title
# print(wangye)

#打印当前页面的URL
# now_url=browser.current_url
# print(now_url)

#定位搜索框(按照id定位法)(可在火狐浏览器中查看原代码)
# ele=browser.find_element_by_id('search-key')
# ele.clear()#清理搜索框中原有的数据
# ele.send_keys('iphone')
# ele.submit()#找到输入框并输入后点提交


#示例2，打开feisu.com
# browser.get(url_3)
# # print(browser.page_source)
# # browser.close()

# #打印网页标题,title后面不能加括号否则报TypeError：'str' object is not callable
# wangye=browser.title
# print(wangye)

# #打印当前页面的URL
# now_url=browser.current_url
# print(now_url)

# #定位搜索框(按照id定位法)(可在火狐浏览器中查看原代码)
# ele=browser.find_element_by_id('CityAjax')
# ele.clear()
# ele.send_keys('35334')
# ele.submit()


# #close all windows
# sleep(5)
# browser.quit()


#登录交换机实例，192.168.1.1/admin/admin

url_4=r'http://192.168.1.1'

#获取当前窗口的句柄
window=browser.current_window_handle
print('old_handle:'+str(window))
#登录
browser.get(url_4)
sleep(2)
ele=browser.find_element_by_id("username")
ele.clear()
ele.send_keys('admin')
sleep(2)
ele=browser.find_element_by_id("password")
ele.clear()
ele.send_keys('admin')
sleep(2)
ele=browser.find_element_by_id('loginbutton')
ele.click()
#ele.send_keys(Keys.ENTER)
sleep(5)
# #弹出新网页之后要获取当前页面的句柄
# window=browser.current_window_handle
# print('new_handle:'+str(window))
# # ele=browser.find_element_by_xpath('/html/body/div/div[3]/div/div[14]/label')
# ele.click()
#browser.switch_to_window(window[-1])

# n = browser.window_handles # 获取当前页句柄
# print (n)
#browser.switch_to.frame()
#browser.switch_to.default_content()
#ele=browser.find_element_by_class_name('wSelect-option wSelect-option-selected')
#ele.click()
ele=browser.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]')
ele.click()
sleep(2)
ele=browser.find_element_by_tag_name('a')
ele.click()
sleep(5)







