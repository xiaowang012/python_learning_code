from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

def setup(url):
    driver=webdriver.Chrome()
    driver.maximize_window()
    #隐式等待
    driver.implicitly_wait(30)
    #get
    driver.get(url)
    try:
        element=driver.find_element_by_id('search-key')
    except:
        print('Error!')
    else:
        element.send_keys()
        element.submit()
        sleep(50)
    
    # handles=driver.window_handles()
    # driver.switch_to_window(handles[-1])


setup('https://home.firefoxchina.cn/')