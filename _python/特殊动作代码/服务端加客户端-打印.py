from utils.win_ctrl import win32
import time, json

def main():
    id1 = self_._widgetSetExecution._currentWidgetSet.get('widget_set_name')
    id2 = self_._currentWidget.get('control_name')
    pdf_url = self_._taskExecution._widgetValues.get(id1).get(id2).get('0').get('0')
    if pdf_url:
        # 打开PDF文件新窗口
        self_._driver.execute_script(r"window.open('" + pdf_url + "')")
        # 采集打开窗口
        while True:
            starttime = time.time()
            print('等待新窗口打开===================================')
            if len(self_._driver.window_handles) > len(
                    self_._taskExecution._openedWindows) or time.time() - starttime > 30:
                break

        wins = self_._driver.window_handles
        print(wins)
        for win in wins:
            if win in self_._taskExecution._openedWindows:
                pass
            else:
                self_._driver.switch_to.window(win)
                self_._taskExecution._currentWindow = win
                self_._taskExecution._openedWindows.append(win)
                self_._taskExecution._windowsData[self_._taskExecution._currentWindow] = {'iframe': ''}
                # 滚动窗口
                if self_._currentWidget.get('window_size') == '0':
                    self_._driver.maximize_window()
        # 置顶

        path = '/session/' + self_._driver.session_id + '/exeCmd'
        url = '%s%s' % (self_._driver.command_executor._url, path)
        data = {
            "p1": "C:/seleniumNode/Python36/pythonw.exe",
            "p2": "C:/upload/runtime_handle.py",
            "p3": "main_client",
            "$this": self_._currentWidget.get('action_code')
        }
        data_str = json.dumps(data)
        result = self_._driver.command_executor._request('POST', url, body=data_str.encode("utf-8"))
        if result.get('status') == 55 or result.get('status') == 500:
            raise Exception(result.get('value'))
        time.sleep(4)

        # 打印完成后关闭PDF文件窗口
        self_._driver.close()
        # 最后一个窗口句柄出队
        popWindow = self_._taskExecution._openedWindows.pop(-1)
        self_._taskExecution._windowsData.pop(popWindow)

        self_._taskExecution._currentWindow = self_._taskExecution._openedWindows[-1]  # 表示从右往左开始
        self_._driver.switch_to.window(self_._taskExecution._currentWindow)
        self_._taskExecution._windowsData[self_._taskExecution._currentWindow] = {'iframe': ''}

def main_client():
    time.sleep(1)
    win32.combination_key("ctrl+p")
    x = win32.win_wait(title='打印', classname='#32770')
    time.sleep(1)
    y = win32.win_wait(x[0], classname='Button', instance=49)
    win32._win_click(y[0])