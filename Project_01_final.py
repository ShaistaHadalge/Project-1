#!/usr/bin/env python
# coding: utf-8

# In[1]:


##TEST-DATA-01

import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(4)
from selenium.webdriver.common.by import By
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(3)
driver.find_element(By.CLASS_NAME,"oxd-button").click()


# In[153]:


##TEST-DATA-02

import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(4)
from selenium.webdriver.common.by import By
driver.find_element(By.NAME,"username").send_keys("Shaista")
driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(3)
driver.find_element(By.CLASS_NAME,"oxd-button").click()


# In[154]:


from selenium.webdriver.common.by import By
message = driver.find_element(By.CLASS_NAME,"oxd-alert-content--error").text
print(message)


# In[155]:


#TEST DATA-03

import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(4)
from selenium.webdriver.common.by import By
driver.find_element(By.NAME,"username").send_keys("Shaista")
driver.find_element(By.NAME,"password").send_keys("admin12345")
time.sleep(3)
driver.find_element(By.CLASS_NAME,"oxd-button").click()


# In[156]:


from selenium.webdriver.common.by import By
message = driver.find_element(By.CLASS_NAME,"oxd-alert-content--error").text
print(message)


# In[151]:


#TEST DATA-03

import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(4)
from selenium.webdriver.common.by import By
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin12345")
time.sleep(3)
driver.find_element(By.CLASS_NAME,"oxd-button").click()


# In[4]:


from selenium.webdriver.common.by import By
message = driver.find_element(By.CLASS_NAME,"oxd-alert-content--error").text
print(message)


# In[5]:


##TEST-DATA-03

import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(4)
from selenium.webdriver.common.by import By
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin12345")
time.sleep(3)
driver.find_element(By.CLASS_NAME,"oxd-button").click()


# In[15]:


message = driver.find_element(By.CLASS_NAME,"oxd-alert-content--error").text
print(message)


# In[210]:


##TEST-DATA-04

import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(4)
from selenium.webdriver.common.by import By
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(3) 
driver.find_element(By.CLASS_NAME,"oxd-button").click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
import time
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
time.sleep(2)
driver.find_element(By.NAME,'firstName').send_keys("shaista")
driver.find_element(By.NAME,'middleName').send_keys("Abdulgani")
driver.find_element(By.NAME,'lastName').send_keys("Hadalge")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()


# In[211]:


driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label/span').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button').click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()


# In[212]:


driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys("shaista Abdulgani Hadalge")
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()


# In[213]:


driver.find_element(By.CLASS_NAME,'oxd-table-cell-action-space').click()


# In[214]:


driver.find_element(By.XPATH,'//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]').click()


# In[ ]:




