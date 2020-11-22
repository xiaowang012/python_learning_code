#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import os
import unittest
from time import sleep
import random


class InputSendkeys():

    def __init__(self,driver):
        self.dr=driver
       
    def send_keys_1(self,element_str,min_num,max_num,default_value,element_save_button):
        '''input keys'''
        alphlist_up=['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
        alphlist_low=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
        symbollist=['!','@','#','$','%','^','&','*','(',')','<','>','?']
        chineselist=['王哈哈','张学友','jack马','薛之谦','二五仔']

        #random
        boundary_value_min=int(min_num)-1
        boundary_value_max=int(max_num)+1
        while True:
            middle_value=random.randint(min_num,max_num)
            if middle_value==min_num or middle_value==max_num:
                pass
            else:
                break
        min_value=min_num
        max_value=max_num
        alph_value_up=random.choice(alphlist_up)+random.choice(alphlist_up)+random.choice(alphlist_up)+random.choice(alphlist_up)
        alph_value_low=random.choice(alphlist_low)+random.choice(alphlist_low)+random.choice(alphlist_low)+random.choice(alphlist_low)
        symbol_value=random.choice(symbollist)+random.choice(symbollist)+random.choice(symbollist)+random.choice(symbollist)+random.choice(symbollist)
        chinese_value=random.choice(chineselist)+random.choice(chineselist)+random.choice(chineselist)

        #alert list
        alertlist_text=[]
        #find input 
        ele=self.dr.find_element_by_name(element_str)
        ele.clear()
        ele.send_keys(boundary_value_min)
        ele_button=self.dr.find_element_by_name(element_save_button)
        ele_button.click()
        a1=self.dr.switch_to_alert()
        a1.accept()
        a2=self.dr.switch_to_alert()
        alertlist_text.append(a2.text)
        a2.accept()

        ele.clear()
        ele.send_keys(boundary_value_max)
        ele_button.click()
        a3=self.dr.switch_to_alert()
        a3.accept()
        a4=self.dr.switch_to_alert()
        alertlist_text.append(a4.text)
        a4.accept()

        ele.clear()
        ele.send_keys(alph_value_low)
        ele_button.click()
        a5=self.dr.switch_to_alert()
        a5.accept()
        a6=self.dr.switch_to_alert()
        alertlist_text.append(a6.text)
        a6.accept()

        ele.clear()
        ele.send_keys(alph_value_up)
        ele_button.click()
        a7=self.dr.switch_to_alert()
        a7.accept()
        a8=self.dr.switch_to_alert()
        alertlist_text.append(a8.text)
        a8.accept()

        ele.clear()
        ele.send_keys(symbol_value)
        ele_button.click()
        a9=self.dr.switch_to_alert()
        a9.accept()
        a10=self.dr.switch_to_alert()
        alertlist_text.append(a10.text)
        a10.accept()

        ele.clear()
        ele.send_keys(chinese_value)
        ele_button.click()
        a11=self.dr.switch_to_alert()
        a11.accept()
        a12=self.dr.switch_to_alert()
        alertlist_text.append(a12.text)
        a12.accept()

        ele.clear()
        ele_button.click()
        a13=self.dr.switch_to_alert()
        a13.accept()
        a14=self.dr.switch_to_alert()
        alertlist_text.append(a14.text)
        a14.accept()

        ele.clear()
        ele.send_keys(min_value)
        ele_button.click()
        a15=self.dr.switch_to_alert()
        a15.accept()
        sleep(20)
        text_1=self.dr.find_element_by_name(element_str).get_attribute('value')
        if text_1==str(min_value):
            br1=True
        else:
            br1=False
        alertlist_text.append(br1)
        
        ele=self.dr.find_element_by_name(element_str)
        ele.clear()
        ele.send_keys(max_value)
        ele_button.click()
        a16=self.dr.switch_to_alert()
        a16.accept()
        sleep(20)
        text_2=ele.get_attribute('value')
        if text_2==str(max_value):
            br2=True
        else:
            br2=False
        alertlist_text.append(br2)
        
        ele=self.dr.find_element_by_name(element_str)
        ele.clear()
        ele.send_keys(middle_value)
        ele_button.click()
        a17=self.dr.switch_to_alert()
        a17.accept()
        sleep(20)
        text_3=ele.get_attribute('value')
        if text_3==str(middle_value):
            br3=True
        else:
            br3=False
        alertlist_text.append(br3)
        
        ele=self.dr.find_element_by_name(element_str)
        ele.clear()
        ele.send_keys(default_value)

        return alertlist_text


    def exit_driver(self):
        self.dr.quit()


class WebTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get('https://hao.360.com/?a1004')
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print(1)
    
    def test_001(self):
        print(2)

    def test_002(self):
        driver=self.driver
        driver_find=InputSendkeys(driver)
        list_1=driver_find.send_keys_1('q',1,10,12)
        #driver_find.exit_driver()
        self.assertEqual(list_1,[xxx,xxx,xxx])

    def test_003(self):
        driver=self.driver
        driver_find=InputSendkeys(driver)
        driver_find.send_keys_1('q',1,10,123)
        #driver_find.exit_driver()
        sleep(5)


if __name__=='__main__':
    unittest.main()

# driver=webdriver.Firefox()
# driver.implicitly_wait(30)
# driver.maximize_window()
# driver.get('https://hao.360.com/?a1004')

# listtext=['aaa','bbb','cccc']
# aaa=InputSendkeys(driver)
# aaa.send_keys_1('q')
#aaa.exit_driver()


while True:
    middle_value=random.randint(1,5)
    if middle_value==1 or middle_value==5:
        pass
    else:
        break

print(middle_value)