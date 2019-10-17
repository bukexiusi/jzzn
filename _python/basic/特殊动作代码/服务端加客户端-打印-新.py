from utils.win_ctrl import win32
import time, json
import win32gui, win32con,win32api
import re, traceback


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

        # 打印完成后关闭PDF文件窗口
        self_._driver.close()
        # 最后一个窗口句柄出队
        popWindow = self_._taskExecution._openedWindows.pop(-1)
        self_._taskExecution._windowsData.pop(popWindow)

        self_._taskExecution._currentWindow = self_._taskExecution._openedWindows[-1]  # 表示从右往左开始
        self_._driver.switch_to.window(self_._taskExecution._currentWindow)
        self_._taskExecution._windowsData[self_._taskExecution._currentWindow] = {'iframe': ''}

class cWindow:
    def __init__(self):
        self._hwnd = None
    def SetAsForegroundWindow(self):
        # First, make sure all (other) always-on-top windows are hidden.
        self.hide_always_on_top_windows()
        win32gui.SetForegroundWindow(self._hwnd)
    def Maximize(self):
        win32gui.ShowWindow(self._hwnd, win32con.SW_MAXIMIZE)
    def _window_enum_callback(self, hwnd, regex):
        '''Pass to win32gui.EnumWindows() to check all open windows'''
        if self._hwnd is None and re.match(regex, str(win32gui.GetWindowText(hwnd))) is not None:
            self._hwnd = hwnd
    def find_window_regex(self, regex):
        self._hwnd = None
        win32gui.EnumWindows(self._window_enum_callback, regex)
    def hide_always_on_top_windows(self):
        win32gui.EnumWindows(self._window_enum_callback_hide, None)
    def _window_enum_callback_hide(self, hwnd, unused):
        if hwnd != self._hwnd: # ignore self
            # Is the window visible and marked as an always-on-top (topmost) window?
            if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) & win32con.WS_EX_TOPMOST:
                # Ignore windows of class 'Button' (the Start button overlay) and
                # 'Shell_TrayWnd' (the Task Bar).
                className = win32gui.GetClassName(hwnd)
                if not (className == 'Button' or className == 'Shell_TrayWnd'):
                    # Force-minimize the window.
                    # Fortunately, this seems to work even with windows that
                    # have no Minimize button.
                    # Note that if we tried to hide the window with SW_HIDE,
                    # it would disappear from the Task Bar as well.
                    win32gui.ShowWindow(hwnd, win32con.SW_FORCEMINIMIZE)


def main_client():
    try:
        regex = ".*PrintPdf.*"
        cW = cWindow()
        cW.find_window_regex(regex)
        cW.Maximize()
        cW.SetAsForegroundWindow()
        # ctrl + p
        win32api.keybd_event(17, 0, 0, 0)  # ctrl
        win32api.keybd_event(80, 0, 0, 0)  # p
        win32api.keybd_event(80, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)

        time.sleep(3)

        regex = "^打印$"
        cW = cWindow()
        cW.find_window_regex(regex)
        cW.Maximize()
        cW.SetAsForegroundWindow()

        win32api.keybd_event(13, 0, 0, 0)  # enter
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
    except:
        print(traceback.format_exc())
        pass

# hwnd_title = dict()
#
# def get_all_hwnd(hwnd, mouse):
#     if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
#         hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})



