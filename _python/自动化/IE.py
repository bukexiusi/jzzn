import time
from selenium import webdriver

driver = webdriver.Ie()
driver.get("http://140.0.1.53:82/zxxt/login.jsp?logout=1")

driver.implicitly_wait(10)
element = driver.find_element_by_xpath('//*[@id="username"]')

element.send_keys("李逍遥")
turn_page_final = filter(str.isdigit, element.get_attribute('value').strip())
turn_page_final = ''.join(list(turn_page_final))
print(turn_page_final)

element.send_keys("赵灵儿")
turn_page_final = filter(str.isdigit, element.get_attribute('value').strip()) # filter(str.isdigit, "filter123") -> 123
turn_page_final = ''.join(list(turn_page_final))
print(turn_page_final)


time.sleep(10)
driver.quit()

# ' //div[@role="navigation"]/ul[2]/li[4]/a'