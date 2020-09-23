#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
chrome_driver_path="/Users/chih-liangyang/Downloads/chromedriver"
#numbers=eval(input("打卡選1  簽退輸入任意鍵"))
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(10)
url="http://ntc.im/pn110/time/timeclock.php"
driver.get(url)
time.sleep(1)
driver.find_element_by_tag_name('select').find_elements_by_tag_name('option')[3].click()
time.sleep(1)
driver.find_element_by_name('employee_passwd').send_keys("1203")
time.sleep(1)
# if numbers==1:
driver.find_element_by_name('left_inout').find_elements_by_tag_name('option')[3].click()
    #簽到
# else:
#     driver.find_element_by_name('left_inout').find_elements_by_tag_name('option')[5].click()
    #簽退
time.sleep(1)
driver.find_element_by_xpath("//*[@id='wrapper']/aside/section/form/div/div[2]/div[6]/button").click()
time.sleep(1)
driver.quit()