import time
from selenium import webdriver

driver = webdriver.Ie()
driver.implicitly_wait(10)
msg = "中12文34"
msgb = msg.encode("utf-8")
msgStr = ""
for i in msgb:
    msgStr = msgStr + str(i) + "zn"
driver.get("http://localhost:8000/document/create/tip?msg=" + msgStr)
# e2 = driver.find_element_by_xpath("//*[@id='su']")
# e2.click()
driver.quit()