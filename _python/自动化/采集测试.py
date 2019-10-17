from selenium import webdriver
import time

def a():
    # driver = webdriver.Chrome()
    driver = webdriver.Ie()
    try:
        driver.get(r'file:///C:\Users\Administrator\Desktop\demo.html')

        xpath = r'//*[@id="n"]/tr'
        driver.implicitly_wait(10)
        va = driver.find_element_by_xpath(xpath)

        print('demo:',va.get_attribute('innerHTML'))
        print('demo111:',type(va.get_attribute('innerText')))
    except Exception as e:
        print(str(e))
    finally:
        driver.quit()

a()