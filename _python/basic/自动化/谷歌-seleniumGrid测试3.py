from selenium import webdriver
import os

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.ie.webdriver import WebDriver

driver = webdriver.Remote(command_executor="http://192.168.0.154:6666/wd/hub",  desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)
driver.get("http://www.baidu.com")