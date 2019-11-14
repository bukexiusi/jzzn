from yt_sys_print import yt_print


def print(*args, sep=' ', end='\n'):
    yt_print(*args, sep=sep, end=end)


def main():
    import time
    import yt
    import datetime
    import copy
    _DATA = "C:\\Users\\admin\\Desktop\\data.xlsx"
    dataLists = yt.execute_data(_DATA)
    for m in range(0, len(dataLists)):
        try:
            rowDatas = dataLists[m]
            print(rowDatas)
            # 执行起始时间
            starttime = datetime.datetime.now()
            # 执行时间
            run_date = int(time.time() * 1000)
            driver = yt.browser.create_driver('IE')
            yt.browser.open_url("https://www.runoob.com/html/html5-new-element.html")
            yt.browser.input({"name": '输入框', "type": "xpath", "attr": '//*[@id="s"]', "iframe": ""}, rowDatas.get("搜索内容"))
            yt.key.send("{ENTER}")
            yt.browser.switch_to_new_window()
            count = yt.browser.element_count(
                {"name": '搜索条数', "type": "xpath", "attr": '/html/body/div[3]/div/div[1]/div[2]/div', "iframe": ""})
            for i in range(count):
                element_info1 = {"name": '采集查询到的内容', "type": "xpath",
                                 "attr": '/html/body/div[3]/div/div[1]/div[2]/div[{index}]/div/h2/a'.format(
                                     index=i + 1), "iframe": ""}
                href = yt.browser.get_attr(element_info1, "href")
                title = yt.browser.get_attr(element_info1, "title")
                yt.browser.click(element_info1)
                yt.browser.switch_to_new_window()
                # 获取表格内容
                table_content_all = []
                el = {"name": '表格', "type": "xpath", "attr": '//*[@id="content"]/table'}
                if yt.browser.check_element(el, timeout=5):
                    count_table = yt.browser.element_count(el)
                    for j in range(count_table):
                        table_content = yt.browser.get_table_by_pandas(el)
                        table_content_all = table_content_all + table_content
                    yt.browser.close()
                else:
                    yt.browser.close()
                    continue
                d1 = copy.copy(rowDatas)
                d1["数据子表名"] = "采集表1"
                f1 = {"搜索内容": rowDatas.get("搜索内容"), "标题": title, "网址": href, "表格内容": table_content_all}
                print(11111111)
                print(rowDatas.get("搜索内容"))
                print(title)
                print(href)
                print(table_content_all)
                print(22222222)
                yt.datasource.save(d1, f1)
            # 执行终止时间
            endtime = datetime.datetime.now()
            # 执行时长
            run_time = (endtime - starttime).seconds
            yt.datasource.save(rowDatas,{"执行时长": run_time, "执行说明": "执行成功", "执行时间": run_date})
            yt.browser.quit()
        except Exception as e:
            yt.browser.quit()
            yt.datasource.save(rowDatas, {"采集内容": "xpath错误","执行说明": "执行失败"+str(e)})
            continue
    yt.dialog.alert("执行成功", title="提示", type="")


if __name__ == "__main__":
    main()
