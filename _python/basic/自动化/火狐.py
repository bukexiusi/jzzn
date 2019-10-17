from selenium import webdriver
fireFox = webdriver.Firefox()
fireFox.get("https://www.baidu.com")

# 通过id定位并输入
fireFox.find_element_by_id("kw").send_keys("李逍遥")
# 通过class定位并点击
fireFox.find_element_by_class_name("s_btn").click()

# 这里是追加‘赵灵儿’到‘李逍遥’后面
fireFox.find_element_by_id("kw").send_keys("赵灵儿")

# xpath定位并输入
fireFox.find_element_by_xpath('//*[@id="kw"]').send_keys("林月如")

js = 'window.open("http://www.sogou.com")'
fireFox.execute_script(js)