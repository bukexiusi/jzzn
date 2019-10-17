from selenium import webdriver

driver = webdriver.Ie()
driver.get("https://www.taobao.com")
driver.refresh()
driver.implicitly_wait(10)
element = driver.find_element_by_xpath('//div[@role="navigation"]/ul[2]/li[4]/a[1]')
element.click()