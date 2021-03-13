# -*- coding: utf-8 -*-
import time
import os
import sys
import urllib
import urllib.request


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
import requests
from PIL import Image



class StartGame():
    def __init__(self):
        chrome_options = Options()
        #chrome_options.add_argument("--window-size=499,800")
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument("--start-maximized")
        prefs = {"profile.managed_default_content_settings.images": 2}
        #chrome_options.add_experimental_option("prefs", prefs)
        self.login_url = 'https://5kings.ru/'
        self.driver = webdriver.Chrome(options=chrome_options,
                                       executable_path=os.getcwd() + './chromedriver')
        
    def switch_to_iframe(self, xpath):
        if xpath:
            self.driver.switch_to.frame(xpath)
            print('Переключились на фрейм меню')
            self.driver.find_element_by_xpath("//input[contains(@value,'Дом Бойцов')]").click()
            #print(self.driver.page_source)
            return True
            
        else:
            return False
            print('Не получилось переключиться на фрейм инвентаря')
            
        
            
        
    
    def login(self):
        self.driver.get(self.login_url)
        self.driver.find_element_by_xpath("//input[contains(@name,'login')]").send_keys('val1n0r')
        self.driver.find_element_by_xpath("//input[contains(@type,'password')]").send_keys('En1996ru')
        self.driver.find_element_by_xpath("//img[contains(@id,'input_button')]").click()
        self.driver.find_element_by_xpath("//img[contains(@id,'input_button')]").click()
        
        # переключаемся на новое окно с игрой
        self.driver.switch_to.window(self.driver.window_handles[1])
        
        # переключаемся на окно действий
        #menu_frame = self.driver.find_element(By.XPATH, '//*[@id="main_div_pers"]/iframe')
        menu_frame = self.driver.find_element(By.XPATH, '//*[@id="d_act"]')
        self.switch_to_iframe(menu_frame) # переключаемся на нужны фрейм
        
        
        
        
            
if __name__ == '__main__':
    st = StartGame()
    st.login()
    
        
        