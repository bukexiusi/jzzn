import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#google浏览器
capabilities = DesiredCapabilities.CHROME
#微软浏览器
#capabilities = DesiredCapabilities.INTERNETEXPLORER
#火狐浏览器
#capabilities = DesiredCapabilities.FIREFOX
capabilities["platform"] = "ANY"

driver = webdriver.Remote(command_executor="http://192.168.0.154:6666/wd/hub",  desired_capabilities=capabilities)
"""
如果grid的hub可以接收到消息，但是测试不成功，则可以使用本地方法来调试。
如driver = webdriver.Ie()来进行本地测试，
"""

# driver = webdriver.Ie()
#driver.implicitly_wait(3)

driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()

time.sleep(5)
driver.quit()