#元素定位
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#实例化浏览器
driver=webdriver.Firefox()
driver.maximize_window()
url=r'http://www.baidu.com'
driver.get(url)

#ID定位
ele=driver.find_element_by_id('kw')
ele.clear()
ele.send_keys('iphone')
ele.submit()
sleep(5)

#name定位
driver.get(url)
ele=driver.find_element_by_name('wd')
ele.clear()
ele.send_keys('huawei')
ele.submit()
sleep(5)

#class_name定位
driver.get(url)
ele=driver.find_element_by_class_name('s_ipt')
ele.clear()
ele.send_keys('xiaomi')
ele.submit()
sleep(5)

#tag_name(标签)定位
driver.get(url)
ele=driver.find_elements_by_tag_name('input')
#ele.clear()
#ele.send_keys('feisu')
#ele.submit()
sleep(5)
print(ele)

#Xpath定位，//*[@id="kw"]
driver.get(url)
ele=driver.find_element_by_xpath('//*[@id="kw"]')
ele.clear()
ele.send_keys('apple')
ele.submit()
sleep(5)

#CSS选择器定位，.soutu-btn（baidu.com的摄像头框，按图片搜索）
driver.get(url)
ele=driver.find_element_by_css_selector('.soutu-btn')
ele.click()

sleep(5)

#Link定位，指定文本，点击学术
driver.get(url)
ele=driver.find_element_by_link_text('学术')
ele.click()

sleep(5)

#partial_link定位，部分文本定位方式
driver.get(url)
ele=driver.find_element_by_partial_link_text('hao123')#
ele.click()

sleep(5)



