import time

import lxml
from selenium import webdriver

chrome = webdriver.Chrome()
# 打开网址
chrome.get("http://www.baidu.com")
chrome.maximize_window()
kw = chrome.find_element_by_xpath("//*[@id='kw']")
kw.send_keys("李逍遥")
time.sleep(5)
chrome.close()

