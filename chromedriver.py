# coding=utf-8
# Version:python3.8.0
# Tools:PyCharm 2018.2.1 x64
__date__ = '2021/4/11 16:54'
__author__ = '张勇'

import time
from selenium import  webdriver


driver = webdriver.Chrome()
driver.get('https://baidu.com')

driver.find_element_by_id('kw').send_keys('python')

driver.find_element_by_id('su').click()

time.sleep(6)

driver.quit()