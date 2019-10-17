import time
from selenium import webdriver
import copy

driver = webdriver.Ie()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://140.0.1.53:82/zxxt/login.jsp")
driver.maximize_window()
driver.maximize_window()
global_handle = driver.current_window_handle

login_btn = driver.find_element_by_xpath("//*[@id='login_submit']")
login_btn.click()

dialog_close = driver.find_element_by_xpath("//*[@id='ext-gen3']/div[12]/table/tbody/tr[1]/td[2]/div[2]")
dialog_close.click()

stay_case = driver.find_element_by_xpath("//*[@title='待执案件']")
stay_case.click()
print("第一次切iframe之前dirver", driver.title)
driver.switch_to.frame(0)
print("第一次切iframe之后dirver", driver.title)
print("第一次-", driver)
cases = driver.find_elements_by_xpath("//table/tbody/tr/td[6]/a")
print("第一次-", cases.__len__())


cases[3].click()
driver.switch_to.window(driver.window_handles[driver.window_handles.__len__() - 1])
driver.close()

driver.switch_to.window(global_handle)
print("第二次-", driver)
driver.switch_to.frame(0)
cases = driver.find_elements_by_xpath("//table/tbody/tr/td[6]/a")
print("第二次-", cases.__len__())
cases[4].click()

driver.quit()
# dialog_close =
# l-dialog-close
