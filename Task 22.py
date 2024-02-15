#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

chrome_service = ChromeService(r"C:\Users\Nancy\OneDrive - ZF Friedrichshafen AG\Desktop\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)
driver.maximize_window()

time.sleep(5)
driver.implicitly_wait(10)

#goto Guvi Instagram page
driver.get('https://www.instagram.com/guviofficial/')

followers= driver.find_element(By.XPATH,"(//span[@class='_ac2a'])[2]/span").text
print("followers:", followers)

following=driver.find_element(By.XPATH,"(//span[@class='_ac2a'])[3]/span").text
print("following:", following)

driver.quit()

