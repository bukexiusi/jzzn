import time
from selenium import webdriver

driver = webdriver.Ie()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")

e1 = driver.find_element_by_xpath("//*[@id='kw']")
e1.send_keys("厦门")
# time.sleep(2)
# e2 = driver.find_element_by_xpath("//*[@id='su']")
# e2.click()
# driver.quit()