# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 17:28:48 2021

@author: Nirmalkumar Rajendran
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import sys

__location__=os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))        
sys.path.append(__location__)
print(__location__)

#getting ssl handshake error , so adding this
caps = webdriver.DesiredCapabilities.CHROME.copy()
caps['acceptInsecureCerts'] = True
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

class twitter:
    
    def __init__(self,username,password,mobile_no):
        self.uname = username
        self.pwd = password
        self.mbl = mobile_no
        self.bot = webdriver.Chrome(desired_capabilities=caps,options=options)
        #self.bot = webdriver.Chrome()
        
    def login(self):
        
        print('login page loading')
        bot = self.bot
        bot.get('https://twitter.com/i/flow/login')
        print('login page loaded')
        time.sleep(15)
        
        print('finding username box')
        email = bot.find_element_by_name("username")
        email.send_keys(self.uname)
        email.send_keys(Keys.RETURN)
        print('entered username box')
        time.sleep(3)
        
        #email = driver.find_element_by_name("text")

        lkUp_strr='please enter your phone number or username to verify it’s you'
        lkUp_strr in bot.page_source
        #lst=list(dir(driver))
        # if(  email.is_displayed() ):
        
        #if(  'phone' in driver.page_source ):
        if(  lkUp_strr in bot.page_source ):
            
            email = bot.find_element_by_name("text")
            print('found double check')
            email.send_keys(self.mbl)
            email.send_keys(Keys.RETURN)
            print('double check done')
            
        time.sleep(3)
        print('sending password')
        pwd = bot.find_element_by_name("password")
        pwd.send_keys(self.pwd)
        pwd.send_keys(Keys.RETURN)
        print('sent password')
        
        #chrome closes soon after api, so sleeping
        time.sleep(100)