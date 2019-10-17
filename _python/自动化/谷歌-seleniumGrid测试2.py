from selenium import webdriver
import os

chrome_driver = os.path.abspath(r"C:\work\webdriver\chromedriver")
os.environ["webdriver.chrome.driver"] = chrome_driver
chrome_capabilities = {
    "browserName": "chrome",  # 浏览器名称
    "version": "",  # 操作系统版本
    "platform": "ANY",  # 平台，这里可以是windows、linux、andriod等等
    "javascriptEnabled": True,  # 是否启用js
    "webdriver.chrome.driver": chrome_driver
}
driver = webdriver.Remote("http://192.168.0.154:5555/wd/hub", desired_capabilities=chrome_capabilities)
# driver.set_window_size(1280,720)
driver.get("http://www.baidu.com")
print(driver.title)
driver.quit()