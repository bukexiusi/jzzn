import time
from selenium import webdriver
import copy

driver = None
try:
    driver = webdriver.Ie()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://140.0.1.53:82/zxxt/login.jsp")
    print("title", driver)
    # driver.switch_to.frame(0)
    print("title", driver)
    driver.maximize_window()
    driver.maximize_window()
finally:
    driver.quit()