import re

# 若有返回值，则返回值存入对应控件中
def main():
    case_code = document_data.get("案号")
    "(2019)闽0203执323号"
    case_code_re = re.findall("(\d{4})", case_code)[0]
    case_code_re = re.findall("\((\d{4})\)", case_code)[0]
    return case_code


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
def main():
    element = WebDriverWait(self_._driver, 20, 0.1).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="kw"]')))
    element.send_keys(Keys.ENTER)