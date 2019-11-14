import time
import yt
import datetime
try:
    # 执行起始时间
    starttime = datetime.datetime.now()
    # 执行时间
    run_date = int(time.time() * 1000)
    driver = yt.browser.create_driver()
    yt.browser.open_url("https://www.runoob.com/html/html5-new-element.html")
    yt.browser.input({"name": '输入框', "type": "xpath", "attr": '//*[@id="s"]', "iframe": ""}, "元素")
    yt.key.send("{ENTER}")
    yt.browser.switch_to_new_window()
    count = yt.browser.element_count({"name": '搜索条数', "type": "xpath", "attr": '/html/body/div[3]/div/div[1]/div[2]/div', "iframe": ""})
    href_all = ""
    title_all = ""
    for i in range(count):
        element_info1 ={"name": '采集查询到的内容', "type": "xpath","attr": '/html/body/div[3]/div/div[1]/div[2]/div[{index}]/div/h2/a'.format(index=i + 1), "iframe": ""}
        href = yt.browser.get_attr(element_info1,"href")
        title = yt.browser.get_attr(element_info1, "title")
        yt.browser.click(element_info1)
        yt.browser.switch_to_new_window()
        # 获取表格内容
        table_content_all = []
        el = {"name": '表格', "type": "xpath", "attr": '//*[@id="content"]/table'}
        el1 = {"name": '箭头', "type": "xpath", "attr": '/html/body/div[3]/div/div[2]/div/div[2]/div[1]/a[1]/i'}
        yuanma = yt.browser.page_source(el1)
        print(yuanma)
        if yt.browser.check_element(el, timeout=5):
            count_table = yt.browser.element_count(el)
            for j in range(count_table):
                table_content = yt.browser.get_table_by_pandas(el)
                table_content_all = table_content_all + table_content
            # print(table_content_all)
            yt.browser.close()
        else:
            yt.browser.close()
            continue
        href_all = href_all + href + ";"
        title_all = title_all + title + ";"
    # print(href_all)
    # print(title_all)
    # 执行终止时间
    endtime = datetime.datetime.now()
    # 执行时长
    run_time = (endtime - starttime).seconds
    yt.browser.quit()
except Exception as e:
    yt.browser.quit()
yt.dialog.alert("执行成功", title="提示", type="")




