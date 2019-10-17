import time

from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains  # 鼠标操作
from selenium.webdriver.common.keys import Keys  # 键盘操作
from selenium.webdriver.support.select import Select  # 下拉操作（从0开始）
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

chrome = webdriver.Chrome()
# 打开网址
chrome.get("http://www.baidu.com")
# 最大化
chrome.maximize_window()
# 通过id定位
kw = chrome.find_element_by_id("kw")
print(kw.get_attribute("id"))
# 输入
kw.send_keys("李逍遥")
time.sleep(1)
# 清空
kw.clear()
time.sleep(1)

kw.send_keys("赵灵儿")
time.sleep(1)

chrome.refresh()
time.sleep(1)

element4 = chrome.find_element_by_link_text('设置')  # 点击文本节点
ActionChains(chrome).move_to_element(element4).perform()  # 鼠标悬停
chrome.find_element_by_link_text('搜索设置').click()
time.sleep(1)
# chrome.find_element_by_xpath("//select[@id='nr']/option[2]").click() # 下拉框直接定位
s = chrome.find_element_by_id('nr')
# s.find_element_by_xpath('//option[@value="50"]').click() # 二次定位
Select(s).select_by_index(1)
# Select(s).select_by_value("50") # Select(s).select_by_value(50)会报错，参数错误，以后用此方法要加引号
time.sleep(1)

# chrome.find_element_by_class_name("pfpanelclose").click()
# chrome.find_element_by_xpath('//*[@class="pfpanelclose close briiconsbg"]').click() # @class=注意点，必须全匹配，这里是全匹配元素的属性
chrome.find_element_by_xpath('//*[contains(@class, "pfpanelclose")]').click()  # 含有class为pfpanelclose的表达式此表达式

# 单选框 以下代码报错
# radios = chrome.find_elements_by_name("SL")
# for radio_ in radios:
#     if not radio_.is_selected():
#         while True:
#             try:
#                 radio_.click()
#                 break
#             except ElementNotVisibleException as e:
#                 print("ElementNotVisibleException", e)
#         time.sleep(1)
# for radio_ in radios:
#     if radio_.get_attribute("value") == 0:
#         if not radio_.is_selected():
#             radio_.click()
#             break

element7 = chrome.find_element_by_xpath('//*[@name="SL" and @value="2"]')
element7.send_keys(Keys.ARROW_DOWN)
# element7 = chrome.find_element_by_xpath('//*[@for="SL_2"]')
# element7 = chrome.find_element_by_id('SL_2')
ActionChains(chrome).click(element7).perform()
time.sleep(3)


# 刷新之后要重新定位元素
kw = chrome.find_element_by_id("kw")
kw.send_keys("赵灵儿")

# 刷新之后要重新定位元素
element4 = chrome.find_element_by_link_text('设置')
ActionChains(chrome).move_to_element(element4).perform()
time.sleep(1)

# 因为搜索框导致的原因必须选择一处空白处鼠标左键点击
# element5 = chrome.find_element_by_xpath('//span[@title="虚拟人物"]') 因为有时候浏览器响应慢，导致此句找不到元素
# ActionChains(chrome).click(element5).perform()
chrome.find_element_by_id('su').click()

element1 = chrome.find_element_by_xpath('//a[contains(text(), "百度百科")]')  # 包含查询样例
# element1a = chrome.find_element_by_xpath('//div[@id="1"]/h3/a') # 轴级查询
ActionChains(chrome).click(element1).perform()
time.sleep(1)

current_handles = chrome.window_handles
chrome.switch_to.window(current_handles[current_handles.__len__() - 1])  # 定位到最新的标签页
element6 = chrome.find_element_by_xpath("//a[text()='分类']")
ActionChains(chrome).move_to_element(element6).perform()
time.sleep(1)
chrome.close()

# js = 'window.open("http://www.sogou.com")'
# chrome.execute_script(js) 此时会报错目标不存在，原因是chrome操作窗口已经关闭，需要重新定位到新的变迁也
# 在当前窗口无法打开，可以新建一个对象打开

chrome2 = webdriver.Chrome()
url = 'file:///E:\总结归纳1\前端\jQuery\单选复选下拉框.html'
chrome2.get(url)
time.sleep(2)
chrome2.close()

# 若想在当前页面打开，可以用执行js的方法 网上说有用 本地测试不通过

current_handles = chrome.window_handles
chrome.switch_to.window(current_handles[0]) # 此句很关键，转移到当前可操作窗口，否则下面的句子执行失败，会显示窗口目标不存在的错误
# js = "window.open(\"" + url + "\")" # 为啥直接执行这句语句就不行？？？是不是open方法不支持打开本地文件协议
js = 'window.open("http://pal6.roogames.com/home/")'
chrome.execute_script(js)

chrome.switch_to.window(chrome.window_handles[1])
chrome.get(url)

# 以下两种方法没有测试成功
# chrome.find_element_by_tag_name("body").send_keys(Keys.CONTROL, 't')
# chrome.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')

time.sleep(5)
chrome.quit()

# 规定长宽
# chrome.set_window_size("211", "119")
# 前进
# chrome.forward()
# 后退
# chrome.back()
# 刷新
# chrome.refresh()
# 截屏
# chrome.get_screenshot_as_file("D:\\img.png")
# 退出
# chrome.close() 结束当前窗口
# chrome.quit()  退出进程
# 进入子iframe
# chrome.switch_to.frame('x-URS-iframe')
# 或
# iframe = browser.find_element_by_tag_name('iframe')
# browser.switch_to.frame(iframe)
# 退出iframe
# chrome.switch_to_default_content()
# 获取当前窗口句柄
# chrome.current_window_handle
# 获取所有窗口句柄
# chrome.window_handles
