#the test for S3900-24T4S
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#firefox
def start_1(url,username,password):
     '''Browser initialization'''
     browser=webdriver.Firefox()
     browser.maximize_window()
   
     #login
     browser.get(url)
     sleep(10)
     ele=browser.find_element_by_id('username')
     ele.clear()
     ele.send_keys(username)

     ele_1=browser.find_element_by_id('password')
     ele_1.clear()
     ele_1.send_keys(password)

     ele_3=browser.find_element_by_id('loginbutton')
     ele_3.click()
     sleep(10)

     'Check the element'
     # ele=browser.find_element_by_xpath('/html/body/div/div[3]/div/div[14]/label').click()
     # sleep(1)
     # ele=browser.find_element_by_xpath('/html/body/div/div[3]/div/div[15]/div[22]/label')
     # print(ele.text)
     # ele.click()
     # print(browser.title)
     # sleep(5)
     
     # ele=browser.find_element_by_tag_name('input')
     # ele=browser.find_element_by_css_selector('html body form#dataForm div#indexContent div.actButtons input#revertButton.actButton')
     # ele.click()
     #ele=browser.find_elements_by_tag_name('td')[0]
     #print(ele)#//*[@id="switchInfoTable_tr0_td1"]
     try:
          ele=browser.find_element_by_xpath('//*[@id="switchInfoTable_tr0_td1"]')
     except:
          print('error')
     else:
          print('pass')
          print(str(ele.text))
start_1('http://192.168.1.1','admin','admin')
sleep(1000)