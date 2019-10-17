# _*_ coding:utf-8 _*_
'''
@author: wangqin
@email: 757748953@qq.com
@time: 2018/12/17 14:02
@File: execute_demo.py
@Description: ***
'''
import pythoncom
from utils import DateHelper
from utils.RemoteWord import Word
from utils.taskmanageutils.Action_set import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from service.widget.widgetservice import *
from service.taskmanagement import execute_document
# from service.client.document_create_v31_思明 import document_third
# from service.client.document_create_v10 import document
from service.varmanagement import var_service
from service.datatable import datatableservice
from utils import ConfigHelper
import re


'''超时时间'''
ExecTimeout = 15

# 第一个控件失效自定义异常
class FirstWidgetTimeoutException(Exception):
    '''新页面第一个控件找不到'''
    pass


# 自定义异常
class StopSetCycle(Exception):
    '''停止集循环'''
    pass


class SwitchIframeCycle(Exception):
    '''切换iframe失败异常'''
    pass

# 任务
class TaskExecution():

    def __init__(self, driver, task, resource, batchParam):
        self._driver = driver
        self._task = task
        self._resource = resource
        self._currentWindow = ''  # 当前浏览器窗口
        self._openedWindows = []  # 打开的窗口句柄数组
        self._windowsData = {}  # 窗口存储信息（如：iframe）
        self._widgetValues = {}  # 控件集值 {id:{id1:[]}}
        self._log = ''  # 记录执行代码流程
        self._log_business = ''  # 记录执行业务流程
        self._execute_error_last = ''  # 记录最后执行错误
        self._widgetDetail = {} # 缓存控件信息
        self._batchParam = batchParam
        # executeIndex 执行序号
        # executeIndexStatus 执行序号状态（第一，其中，最后，唯一）
        # currentTime 当前时间戳
        self._newWindow = False # 新窗口标识


    # 执行任务
    def excuteTask(self):
        self._log = self._log + '当前任务名称：' + self._task.get('task_name') + "<br/>"
        self._log_business = self._log_business + "当前任务名称：" + self._task.get('task_name') + "<br/>"

        # 窗口最大化
        window_size = self._task.get('window_size')
        if window_size and window_size == "0":
            self._driver.maximize_window()
        # self._driver.implicitly_wait(10)
        # 起始网址
        start_url = self._task.get('start_url')
        if "文书生成" in self._task.get("task_name"):
            case_index = self._batchParam.get("executeIndex") + 1
            msg = "当前正在执行第%s个案件，案号：%s，请耐心等待！" % (case_index, self._resource.get("案号"))
            msgb = msg.encode("utf-8")
            msgStr = ""
            for i in msgb:
                msgStr = msgStr + str(i) + "zn"
            start_url = "".join(["http://",
                                 ConfigHelper.HOST_IP,
                                 ":",
                                 str(ConfigHelper.HOST_PORT),
                                 "/document/create/tip?msg=",
                                 msgStr])
            self._driver.get(start_url)
        else:
            self._driver.get(start_url)
            # 收集打开的窗口句柄
            self._currentWindow = self._driver.current_window_handle
            self._openedWindows.append(self._currentWindow)
            self._windowsData[self._currentWindow] = {'iframe': ''}
            # 滚动窗口
            self._driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            self._driver.execute_script('window.scrollTo(0,0)')

        # 获取步骤
        steps = self._task.get('steps')
        if len(steps) >= 1:
            # 默认取第一个为开始步骤
            step = steps[0]
            # 执行当前步骤
            stepExecution = StepExecution(self, step)
            stepExecution.executeStep()
        else:
            print('无步骤...')

    # 过滤条件
    def _conditionFilter(self, filter_conditions, currentWidgetSet):
        # 存放最终结果
        flag = True
        # 保存比较结果
        filter_condition_result = {}
        if filter_conditions.__len__() > 0:
            for filter_condition in filter_conditions:
                # 获取比较左右比较内容比较返回结果
                if filter_condition.get("condition_type") == "SET_CIRCLE":
                    # 集循环条件
                    element_index = currentWidgetSet.get('ignore_cycle_index')
                    ignore_cycle_index = filter_condition.get("ignore_cycle_index")
                    ignore_cycle_index_array = ignore_cycle_index.split(";")
                    if str(element_index) in ignore_cycle_index_array:
                        flag = True
                        element_index = element_index + 1
                        currentWidgetSet['ignore_cycle_index'] = element_index
                    else:
                        flag = self._getCompareRes(filter_condition, currentWidgetSet)
                else:
                    # 控件条件
                    flag = self._getCompareRes(filter_condition, currentWidgetSet)

                filter_condition_result[filter_condition.get("group")] = flag.__str__()

            print("filter_condition_result:", filter_condition_result)
            # 获取逻辑表达式并计算
            logical_expression = filter_conditions[0].get("logical_expression")
            for k, v in filter_condition_result.items():
                print('k=', k, 'v=', v)
                logical_expression = logical_expression.replace(k, v)
            print("logical_expression:", logical_expression)
            if logical_expression:
                flag = eval(logical_expression)
        return flag

    # 获取比较内容进行比较返回结果
    def _getCompareRes(self, condition, currentWidgetSet):
        # 比较符号
        symbol = condition.get('symbol')
        # 比较类型  TODO 默认文本比较
        collect_value_type = 'TEXT'

        # 判断是否number类型的正则
        reg = re.compile(r'^[-+]?[0-9]+\.[0-9]+$|^[-+]?[0-9]+$')
        # 处理左侧值  ==== START
        data_handle_type = condition.get('data_handle_type')    # 数据类型
        if not data_handle_type:
            data_handle_type = 'TEXT'
        # 获取左边的比较内容
        # 判断比较的值是具体值还是外部数据源
        outerKeyLeft = condition.get('value_temporary_left')
        if outerKeyLeft:
            leftValue = self._getResourceValue(outerKeyLeft)
        else:
            leftValue = self._getBrowserLeftValue(condition, currentWidgetSet)
            tempWidget = self._widgetDetail.get(condition.get('widget_id_left'))
            if tempWidget:
                collect_value_type = tempWidget.get('collect_value_type')
            collect_value_type = collect_value_type if collect_value_type else 'TEXT'
        if condition.get('value_left'):
            leftValue = condition.get('value_left')
        # 判断是否存在left数据处理情况
        if leftValue:
            # 判断是否有数据处理表达式
            if condition.get('data_handle_expression_left'):
                temp = condition.get('data_handle_expression_left')
                if temp.startswith(r're'):
                    temp = temp.replace(r'$', "'" + leftValue + "'")
                    leftValue = eval(temp)
                else:
                    if data_handle_type == 'NUMBER':
                        temp = temp.replace(r'$', str(leftValue))
                        leftValue = eval(temp)
                    elif data_handle_type == 'TEXT':
                        temp = temp.replace(r'$',leftValue)
                        leftValue = temp
            else:
                if data_handle_type == 'NUMBER':
                    leftValue = eval(str(leftValue))
                elif data_handle_type == 'TEXT':
                    leftValue = leftValue
        # 处理左侧值  ==== END

        # 处理右侧值  ==== START
        # 获取右边的比较内容
        outerKeyRight = condition.get('value_temporary_right')
        if outerKeyRight:
            rightValue = self._getResourceValue(outerKeyRight)
        else:
            rightValue = self._getBrowserRightValue(condition, currentWidgetSet)
            tempWidget = self._widgetDetail.get(condition.get('widget_id_right'))
            if tempWidget:
                collect_value_type = tempWidget.get('collect_value_type')
            collect_value_type = collect_value_type if collect_value_type else 'TEXT'
        if condition.get('value_right'):
            rightValue = condition.get('value_right')
        if rightValue:
            # 判断是否有数据处理表达式
            if condition.get('data_handle_expression_right'):
                temp = condition.get('data_handle_expression_right')
                if temp.startswith(r're'):
                    temp = temp.replace(r'$', "'" + rightValue + "'")
                    rightValue = eval(temp)
                else:
                    if data_handle_type == 'NUMBER':
                        temp = temp.replace(r'$', str(rightValue))
                        rightValue = eval(temp)
                    elif data_handle_type == 'TEXT':
                        temp = temp.replace(r'$', rightValue)
                        rightValue = temp
            else:
                if data_handle_type == 'NUMBER':
                    rightValue =  eval(str(rightValue))
                elif data_handle_type == 'TEXT':
                    rightValue =  rightValue
        # 处理右侧值  ==== END

        # 比较
        print('leftValue=', leftValue, 'rightValue=', rightValue)
        flag = self._compare_value(leftValue, rightValue, symbol, data_handle_type)
        return flag

    # 左边比较内容值获取
    def _getBrowserLeftValue(self, condition, currentWidgetSet):
        # 条件值获取widgetId 获取控件
        widgetName = condition.get('widget_name_left')
        widgetsetName = condition.get('widget_set_name_left')
        if not (widgetName and widgetsetName):
            return ''
        symbol = condition.get('symbol')

        totalArray = ["10", "14", "15", "16", "17", "18", "19"]  # 全
        pageArray = ["11", "20", "21", "22", "23", "24", "25"]  # 分页
        if symbol in totalArray:
            # 控件所有值
            result_array = []
            pageValues = self._widgetValues.get(widgetsetName)  # 分页数组
            if not pageValues:
                return None
            vv = pageValues.get(widgetName)  # 控件
            if not vv:
                return None
            for k, v in vv.items():  # 页循环
                if isinstance(v, dict):
                    for k_, v_ in v.items():  # 行循环
                        if isinstance(v_, list):
                            for v_temp in v_:
                                result_array.append(v_temp)
                        else:
                            result_array.append(v_)
            print('pageValues=========', pageValues)
            print("全数组:", result_array)
            return result_array
        elif symbol in pageArray:
            # 条件控件集所有值
            result_array = []
            pageValues = self._widgetValues.get(widgetsetName)  # 分页数组
            if not pageValues:
                return None
            vv = pageValues.get(widgetName)  # 控件
            if not vv:
                return None

            turn_page_index = currentWidgetSet.get('turn_page_index')
            v = vv.get(turn_page_index)  # 获取当前页
            for k_, v_ in v.items():  # 行循环
                if isinstance(v_, list):
                    for v_temp in v_:
                        result_array.append(v_temp)
                else:
                    result_array.append(v_)
            print('pageValues=========', pageValues)
            print("全数组:", result_array)
            return result_array
        else:
            pageValues = self._widgetValues.get(widgetsetName)  # 分页数组
            if not pageValues:
                return None
            widgetValues = pageValues.get(widgetName)
            if not widgetValues:
                return None
            turn_page_index = currentWidgetSet.get('turn_page_index')  # 分页索引
            browserValues = widgetValues.get(turn_page_index)  # 页面数组
            browserValues = browserValues if browserValues else (
                widgetValues.get('0') if widgetValues.get('0') else widgetValues.get(None))
            # 页面索引
            idx = currentWidgetSet.get('row_index') if currentWidgetSet.get(
                "is_collect_single") else currentWidgetSet.get('element_idx')
            result = browserValues.get(str(idx))
            result = result if result else (
                browserValues.get('0') if browserValues.get('0') else browserValues.get(None))
            return result

    # 右边比较内容值获取
    def _getBrowserRightValue(self, condition, currentWidgetSet):
        # 条件值获取widgetId 获取控件
        widgetName = condition.get('widget_name_right')
        widgetsetName = condition.get('widget_set_name_right')
        if not (widgetName and widgetsetName):
            return ''
        symbol = condition.get('symbol')

        if symbol == "10":
            # 控件所有值
            result_array = []
            pageValues = self._widgetValues.get(widgetsetName)  # 分页数组
            if not pageValues:
                return None
            vv = pageValues.get(widgetName)  # 控件
            if not vv:
                return None
            for k, v in vv.items():  # 页循环
                if isinstance(v, dict):
                    for k_, v_ in v.items():  # 行循环
                        if isinstance(v_, list):
                            for v_temp in v_:
                                result_array.append(v_temp)
                        else:
                            result_array.append(v_)
            print('pageValues=========', pageValues)
            print("全数组:", result_array)
            return result_array
        elif symbol == "11":
            # 当前控件集所有值
            result_array = []
            pageValues = self._widgetValues.get(widgetsetName)  # 分页数组
            if not pageValues:
                return None
            vv = pageValues.get(widgetName)  # 控件
            if not vv:
                return None
            turn_page_index = currentWidgetSet.get('turn_page_index')
            v = vv.get(turn_page_index)  # 获取当前页
            for k_, v_ in v.items():  # 行循环
                if isinstance(v_, list):
                    for v_temp in v_:
                        result_array.append(v_temp)
                else:
                    result_array.append(v_)
            print('pageValues=========', pageValues)
            print("全数组:", result_array)
            return result_array
        else:
            pageValues = self._widgetValues.get(widgetsetName)  # 分页数组
            if not pageValues:
                return None
            widgetValues = pageValues.get(widgetName)
            if not widgetValues:
                return None

            turn_page_index = currentWidgetSet.get('turn_page_index')  # 分页索引
            browserValues = widgetValues.get(turn_page_index)  # 页面数组
            browserValues = browserValues if browserValues else (
                widgetValues.get('0') if widgetValues.get('0') else widgetValues.get(None))

            # 页面索引
            idx = currentWidgetSet.get('row_index') if currentWidgetSet.get(
                "is_collect_single") else currentWidgetSet.get('element_idx')
            result = browserValues.get(str(idx))
            result = result if result else (
                browserValues.get('0') if browserValues.get('0') else browserValues.get(None))
            return result

    # 获取数据源值
    def _getResourceValue(self, outerKey):
        # if ',' in outerKey:
        #     keys = []
        #     key = outerKey.split(',')[2]
        #     keys.append(key)
        # else:
        keys = outerKey.split('.')
        temp = self._resource
        print(temp)
        if len(keys) > 1:
            for k in range((len(keys))):
                key = keys[k]
                temp2 = temp[key]
                if (isinstance(temp2, list)):
                    idx = temp[key + '_idx']  # 当前数组指定的序号
                    temp = temp2[idx]
                else:
                    temp = temp2
            return temp
        else:
            return temp[keys[0]]

    # 获取控件集数据
    def _getWidgetValue(self, input_condition, page_index, row_index):
        collect_value = self._widgetValues
        widget_set_value = collect_value.get(input_condition.get("widget_set_name_right"))
        if not widget_set_value:
            return ''
        widget_value = widget_set_value.get(input_condition.get("widget_name_right"))
        if not widget_value:
            return ''
        if not page_index and not row_index:
            page_index = 0
            row_index = 0
        page_value = widget_value.get(page_index)
        if not page_value:
            return ''
        row_value = page_value.get(row_index)
        if not row_value:
            return ''
        return row_value

    # 比较函数 type: 数据类型，TEXT,NUMBER,DATE...
    def _compare_value(self, value1, value2, symbol, type):
        print('内容比较：value1==', value1, '---value2==', value2)

        if symbol == '7':  # 为空
            if value1:
                return False
            else:
                return True

        if symbol == '12':  # 不为空
            if value1:
                return True
            else:
                return False

        if not value1 and not value2:
            return True

        if type == 'TEXT':  # 文本
            if not value1:
                value1 = ''
            if not value2:
                value2 = ''

            if symbol == '3':
                return value1 == value2
            elif symbol == '6':
                return value1 != value2
            elif symbol == '8':  # 包含
                return value2 in value1
            elif symbol == '9':
                return value1 in value2
            elif symbol == '10' or symbol == '11':
                if isinstance(value1, list):  # 数组包含
                    for t in value1:
                        if value2 in t:  # 数组值包含
                            return True
                return False
            elif symbol == '7':  # 为空
                if value1:
                    return False
                else:
                    return True
            elif symbol == '12':  # 不为空
                if value1:
                    return True
                else:
                    return False
            elif symbol == '13':  # 不包含
                return not value2 in value1

        elif type == 'NUMBER':  # 数字
            if not value1 or value1 == 'null' or value1 == 'NULL':
                value1 = 0
            if not value2 or value2 == 'null' or value2 == 'NULL':
                value2 = 0

            if not isinstance(value1, list):
                value1 = float(value1)

            if not isinstance(value2, list):
                value2 = float(value2)

            if symbol == '2':
                return value1 >= value2
            elif symbol == '1':
                return value1 > value2
            elif symbol == '3':
                return value1 == value2
            elif symbol == '6':
                return value1 != value2
            elif symbol == '5':
                return value1 <= value2
            elif symbol == '4':
                return value1 < value2
            elif symbol == '10' or symbol == '11':
                if isinstance(value1, list):
                    for t in value1:
                        if t == value2:
                            return True
                return False
            elif symbol == "14" or symbol == "20":
                v1_total = 0
                if isinstance(value1, list):
                    for t in value1:
                        v1_total = v1_total + float(t)
                    return v1_total > value2
                return False
            elif symbol == "15" or symbol == "21":
                v1_total = 0
                if isinstance(value1, list):
                    for t in value1:
                        v1_total = v1_total + float(t)
                    return v1_total >= value2
                return False
            elif symbol == "16" or symbol == "22":
                v1_total = 0
                if isinstance(value1, list):
                    for t in value1:
                        v1_total = v1_total + float(t)
                    return v1_total == value2
                return False
            elif symbol == "17" or symbol == "23":
                v1_total = 0
                if isinstance(value1, list):
                    for t in value1:
                        v1_total = v1_total + float(t)
                    return v1_total < value2
                return False
            elif symbol == "18" or symbol == "24":
                v1_total = 0
                if isinstance(value1, list):
                    for t in value1:
                        v1_total = v1_total + float(t)
                    return v1_total < value2
                return False
            elif symbol == "19" or symbol == "25":
                v1_total = 0
                if isinstance(value1, list):
                    for t in value1:
                        v1_total = v1_total + float(t)
                    return v1_total != value2
                return False
        elif type == 'DATE':  # 日期
            pass


# 步骤
class StepExecution():

    def __init__(self, taskExecution, step, parentWidgetExecution=None):
        self._parentWidgetExecution = parentWidgetExecution  # 来源控件（目前用于分页循环、页面循环）
        self._taskExecution = taskExecution
        self._currentStep = step
        self._driver = self._taskExecution._driver
        print('当前步骤名称：', self._currentStep.get('step_name'))
        self._taskExecution._log = self._taskExecution._log + '当前步骤名称：' + self._currentStep.get('step_name') + "<br/>"

    # 执行步骤
    def executeStep(self):
        # 获取控件集
        widgetSets = self._currentStep.get('widget_sets')  # list
        # 循环控件集
        for idx in range(0, len(widgetSets)):
            # 当前控件集
            widgetSet = widgetSets[idx]
            # 执行当前控件集
            widgetSetExecution = WidgetSetExecution(self, widgetSet)
            widgetSetExecution.executeWidgetSet()

        # 若存在下一步骤，则执行下一步骤
        nextStepId = self._currentStep.get('next_step_id')
        if nextStepId:
            nextStep = self.getNextStep(nextStepId)
            # 设置当前执行的步骤
            if nextStep != None:
                stepExecution = StepExecution(self._taskExecution, nextStep)
                stepExecution.executeStep()
            else:
                print(self._currentStep.get('step_name'), '无下一步')

    # 获取下一步骤
    def getNextStep(self, step_id):
        steps = self._taskExecution._task.get('steps')
        for idx in range(len(steps)):
            step = steps[idx]
            if step.get('id') == step_id:
                return step
        return None

    # 切换iframe窗口
    def switchIframe(self, iframeStr, timeout=ExecTimeout):
        windowData = self._taskExecution._windowsData[self._taskExecution._currentWindow]
        currentIframe = windowData.get('iframe')

        # 判断当前窗口中，目前的iframe是否与要切换的一致，包含空信息  todo 需要确认下，两个空信息是否会相等
        if currentIframe == iframeStr:
            return False
        else:
            windowData['iframe'] = iframeStr

            if not iframeStr:
                # 目标iframe为空，回到根目录即可
                self._driver.switch_to_default_content()
            else:
                if currentIframe and iframeStr.startswith(currentIframe):
                    # 目标iframe为当前iframe的子目录，则直接从当前iframe继续往下切换
                    iframeStr = iframeStr.replace(currentIframe + ';', '')
                    self.__switchIframeCircle(iframeStr, timeout)
                else:
                    self._driver.switch_to_default_content()
                    self.__switchIframeCircle(iframeStr, timeout)

            return True

    # 循环切换iframe
    def __switchIframeCircle(self, iframeStr, timeout=ExecTimeout, WaitFq=0.1):
        # ;号分割，格式 1;2;3...
        iframes = iframeStr.split(';')
        for iframe in iframes:
            try:
                temp = int(iframe)
            except Exception:
                temp = iframe

            waitTotalTime = 0
            while True:
                try:
                    self._driver.switch_to.frame(temp)
                    break
                except:
                    if waitTotalTime > timeout:
                        raise SwitchIframeCycle()
                waitTotalTime = waitTotalTime + WaitFq
                time.sleep(WaitFq)


class WidgetSetExecution():

    def __init__(self, stepExecution, widgetSet):
        self._stepExecution = stepExecution
        self._currentWidgetSet = widgetSet
        self._taskExecution = self._stepExecution._taskExecution
        self._driver = self._taskExecution._driver
        print('控件集名称：', self._currentWidgetSet.get('widget_set_name'))
        self._taskExecution._log = self._taskExecution._log + '当前控件集名称：' + self._currentWidgetSet.get(
            'widget_set_name') + "<br/>"

    # 执行控件集
    def executeWidgetSet(self):
        self.__executeWidgetSetPageCircle()

    # 控件集翻页循环（需要考虑页面元素循环、数据源循环）
    def __executeWidgetSetPageCircle(self):
        # 判断是否有翻页
        is_exist_turn_page = self._currentWidgetSet.get('is_exist_turn_page')
        if is_exist_turn_page:  # 存在翻页
            turn_page_start = int(self.__getTurnPageStart())
            turn_page_final = int(self.__getTurnPageFinal())

            if turn_page_start != 1:
                # todo 起始页不为首页，则需要处理（要么一页一页往下翻，要么输入页数，点查询，直接定位那一页）
                pass

            if turn_page_final:
                for index in range(turn_page_start, turn_page_final + 1):
                    if index >= turn_page_start + 1:
                        self.__executeNexPage()

                    self.__setWidgetSetPageIndex(index)  # 记录翻页下标
                    end_circle = self.__executeWidgetSetElementCircle()  # 先执行一次页面循环，再进行翻页
                    if end_circle:
                        break
            else:
                index = turn_page_start
                while True:
                    self.__setWidgetSetPageIndex(index)  # 记录翻页下标
                    end_circle = self.__executeWidgetSetElementCircle()  # 先执行一次页面循环，再进行翻页
                    if end_circle:
                        break
                    # 找到翻页元素
                    try:
                        self.__executeNexPage()
                    except Exception as e:
                        break  # 跳出循环
                    index = index + 1
        else:
            self.__setWidgetSetPageIndex()
            self.__executeWidgetSetElementCircle()

    # 设置分页索引
    def __setWidgetSetPageIndex(self, index=0):
        if self._stepExecution._parentWidgetExecution:
            parentWidgetSet = self._stepExecution._parentWidgetExecution._widgetSetExecution._currentWidgetSet
            self._currentWidgetSet['turn_page_index'] = parentWidgetSet.get('turn_page_index') + "-" + \
                                                        str(parentWidgetSet.get('element_idx')) + '-' + str(index)
        else:
            self._currentWidgetSet['turn_page_index'] = str(index)

    # 翻页
    def __executeNexPage(self):
        self.__switchWigetSetPageIframe()

        turn_page_xpath = self._currentWidgetSet.get('turn_page_xpath')
        element = WebDriverWait(self._driver, ExecTimeout, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, turn_page_xpath)))
        element.click()

    # 获取翻页末页
    def __getTurnPageFinal(self):
        turn_page_final = self._currentWidgetSet.get('turn_page_final')
        if turn_page_final:
            return turn_page_final
        else:
            turn_page_final_xpath = self._currentWidgetSet.get('turn_page_final_xpath')
            if turn_page_final_xpath:
                self.__switchWigetSetPageIframe()
                element = WebDriverWait(self._driver, ExecTimeout, 0.1).until(
                    EC.visibility_of_element_located((By.XPATH, turn_page_final_xpath)))
                while True:
                    turn_page_final = filter(str.isdigit, element.get_attribute('value').strip())
                    turn_page_final = ''.join(list(turn_page_final))
                    if turn_page_final:
                        break
                return turn_page_final
            return "1"

    # 获取翻页首页
    def __getTurnPageStart(self):
        turn_page_start = self._currentWidgetSet.get('turn_page_start')
        if turn_page_start:
            return turn_page_start
        else:
            turn_page_start_xpath = self._currentWidgetSet.get('turn_page_start_xpath')
            if turn_page_start_xpath:
                self.__switchWigetSetPageIframe()

                element = WebDriverWait(self._driver, ExecTimeout, 0.1).until(
                    EC.visibility_of_element_located((By.XPATH, turn_page_start_xpath)))
                turn_page_start = filter(str.isdigit, element.get_attribute('value').strip())
                turn_page_start = ''.join(list(turn_page_start))
                return turn_page_start
            return 1

    # 切换页面iframe
    def __switchWigetSetPageIframe(self):
        self._stepExecution.switchIframe(self._currentWidgetSet.get('turn_page_iframe'))

    # 控件集页面元素循环（需要考虑数据源循环）
    def __executeWidgetSetElementCircle(self):
        # 判断控件集是否单条采集
        is_collect_single = self._currentWidgetSet.get('is_collect_single')
        # 退出循环(包括翻页)
        if is_collect_single:  # 单条采集
            self._currentWidgetSet['element_idx'] = '0'
            self.__executeWidgetSetResourceCircle()
        else:  # 循环采集
            # 执行当前控件集
            self.__circleExecuteBrowserElements()

    # 控件集页面元素循环（需要考虑数据源循环）
    def __executeWidgetSetResourceCircle(self):
        # 控件预处理
        maxOuterKey, maxWidgetCircleTimes = self.__widgetPretreatment()
        # 确定控件集循环次数
        circle_outer = self.__getWidgetSetResourceCircle(maxOuterKey)
        circle_widget = {"times": maxWidgetCircleTimes}
        circle = circle_outer if circle_outer.get("times") > circle_widget.get("times") else circle_widget

        for idx in range(circle.get('times')):
            self._currentWidgetSet["row_index"] = str(idx)
            self.__executeWidgetSetResource()

    # 页面元素循环
    def __circleExecuteBrowserElements(self):
        xpath = self._currentWidgetSet.get('parent_xpath')
        self.__switchWidgetSetBrowserIframe()
        # 所有元素
        elements = WebDriverWait(self._driver, ExecTimeout, 0.1).until(EC.visibility_of_all_elements_located((By.XPATH, xpath)))
        cycle_index_step = int(self._currentWidgetSet.get("cycle_index_step")) if self._currentWidgetSet.get(
            "cycle_index_step") else 1
        if cycle_index_step > 0:
            cycle_index_start = int(self._currentWidgetSet.get("cycle_index_start")) if self._currentWidgetSet.get(
                "cycle_index_start") else 0
            cycle_index_end = int(self._currentWidgetSet.get("cycle_index_end")) if self._currentWidgetSet.get(
                "cycle_index_end") else len(elements)
        else:
            cycle_index_start = int(self._currentWidgetSet.get("cycle_index_start")) if self._currentWidgetSet.get(
                "cycle_index_start") else len(elements) - 1
            cycle_index_end = int(self._currentWidgetSet.get("cycle_index_end")) if self._currentWidgetSet.get(
                "cycle_index_end") else -1

        self._currentWidgetSet["ignore_cycle_index"] = 0
        for idx in range(cycle_index_start, cycle_index_end, cycle_index_step):
            # for idx in range(len(elements)):
            self._currentWidgetSet['element_idx'] = str(idx)
            print('======================循环================', self._currentWidgetSet)
            # 获取集循环条件值
            conditions = self._getSetConditionFilter()

            has_set_cycle_conditions = len(conditions) > 0
            if has_set_cycle_conditions:
                # 若有循环条件，则设置循环条件
                self.__setCycleCondition()
            try:
                self.__executeWidgetSetResourceCircle()
            except StopSetCycle:
                # 捕捉到异常则跳出循环
                break
            except Exception as e:
                raise e

    # 设置循环条件
    def __setCycleCondition(self):
        widgets = self._currentWidgetSet.get('widgets')
        idx_set = 0
        for idx in range(len(widgets)):
            widget = widgets[idx]
            collect_xpath = widget.get("collect_xpath")
            if not collect_xpath:
                break
            idx_set = idx

        widget_set = widgets[idx_set]
        widget_set["has_set_cycle_conditions"] = True

    # 获取集FILTER的条件值
    def _getSetConditionFilter(self):
        conditionValues = self._currentWidgetSet.get('condition_values')
        filter_conditions = []
        if conditionValues:
            for conditionValue in conditionValues:
                if conditionValue.get('condition_type') == 'SET_CIRCLE':
                    filter_conditions.append(conditionValue)
        return filter_conditions

    # 切换页面iframe
    def __switchWidgetSetBrowserIframe(self):
        self._stepExecution.switchIframe(self._currentWidgetSet.get('parent_iframe'))

    # 控件预处理
    def __widgetPretreatment(self):
        maxOuterKey = None  # 最长层级的外部数据源
        maxWidgetCircleTimes = 1  # 控件值循环次数
        widgets = self._currentWidgetSet.get('widgets')  # 控件数组
        for widget in widgets:
            actionType = widget.get('action_type')  # 动作类型
            # 置入采集类型到全局变量中
            widgetMapping = self._taskExecution._widgetDetail
            collect_value_type = widget.get("collect_value_type")
            if collect_value_type:
                widgetMapping[widget.get("id")] = {"collect_value_type": collect_value_type}
                self._taskExecution._widgetDetail = widgetMapping
            # 判断是否输入或下拉选择动作，是则找出INPUT的内容,取第一条，数据有且只有一条
            if actionType == '5' or actionType == '6' or actionType == '2' or actionType == '7' or actionType == '8':
                input_condition = None
                # 获取条件值
                condition_values = widget.get('condition_values')
                for condition_value in condition_values:
                    if condition_value.get('condition_type') == 'INPUT':
                        input_condition = condition_value
                        break
                # 判断输入内容值是来自外部数据源还是具体值
                if input_condition:
                    # 外部数据源决定循环次数
                    outerKey = input_condition.get('value_temporary_right')
                    if outerKey:
                        # 根据字典找到具体的值 outerKey 格式: name1.name2.name3...
                        if (maxOuterKey == None or (len(outerKey.split('.')) > len(maxOuterKey.split('.')))):
                            maxOuterKey = outerKey
                    else:
                        # 控件决定循环次数
                        collect_value = self._taskExecution._widgetValues
                        widget_set_value = collect_value.get(input_condition.get("widget_set_name_right"))
                        if not widget_set_value:
                            continue
                        widget_value = widget_set_value.get(input_condition.get("widget_name_right"))
                        if not widget_value:
                            continue
                        cycle_times = 0
                        for page_k, page_v in widget_value.items():
                            for row_k, row_v in page_v.items():
                                cycle_times = cycle_times + 1
                        maxWidgetCircleTimes = cycle_times if cycle_times > maxWidgetCircleTimes else maxWidgetCircleTimes
        return maxOuterKey, maxWidgetCircleTimes

    # 获取控件集下的数据源循环信息
    def __getWidgetSetResourceCircle(self, outerKey):
        circle = {
            'times': 1
        }
        if outerKey == None:
            return circle
        # name.name1.name2
        # len(keys) - 2 -> name1：即父节点
        # len(key2) - 3 -> name：即父节点的父节点
        keys = outerKey.split('.')
        temp = self._taskExecution._resource
        for k in range((len(keys) - 1)):  # 循环 name name1
            key = keys[k]
            if (k == len(keys) - 2):  # 父节点
                circle['parent'] = temp  # 设置循环集合的父节点

            temp2 = temp[key]
            if (isinstance(temp2, list) and k < len(keys) - 2):  # 父节点无需指定数组元素
                idx = temp[key + '_idx']  # 当前数组指定的序号
                temp = temp2[idx]
            else:
                temp = temp2

            if (k == len(keys) - 2):
                circle['key'] = keys[k]  # 设置循环集合Key
                circle['times'] = len(temp)  # 设置循环集合的长度
        return circle

    # 执行控件集数据源
    def __executeWidgetSetResource(self):
        # 所有控件
        widgets = self._currentWidgetSet.get('widgets')
        for idx in range(len(widgets)):
            # 当前控件
            widget = widgets[idx]
            # 执行当前控件
            widgetExecution = WidgetExecution(self, widget)
            widgetExecution.executeWidget()


# 控件
class WidgetExecution():

    def __init__(self, widgetSetExecution, widget):
        self._currentWidget = widget
        self._widgetSetExecution = widgetSetExecution
        self._driver = self._widgetSetExecution._driver
        self._taskExecution = self._widgetSetExecution._taskExecution
        self._stepExecution = self._widgetSetExecution._stepExecution
        print('当前控件名称：', self._currentWidget.get('control_name'))
        self._taskExecution._log = self._taskExecution._log + '当前控件名称：' + self._currentWidget.get(
            'control_name') + "<br/>"

    # 执行控件
    def executeWidget(self):
        # 记录执行业务日志
        if self._currentWidget.get('log'):
            self._taskExecution._log_business = self._taskExecution._log_business + self._currentWidget.get(
                'log') + "<br/>"

        # 延迟等待
        self.__widgetDelay()
        print('延迟等待结束....')

        # 执行动作 成功执行返回True,否则返回False
        res = False
        try:
            res = self.__handle_widget()
        # except FirstWidgetTimeoutException:
        #     print('新页面第一个控件没找到。。。控件名称：',self._currentWidget.get('control_name'))
        #     # 刷新页面再次执行
        #     self._driver.execute_script(r"window.location.reload()")
        #     time.sleep(1)
        #     self._driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        #     self._driver.execute_script('window.scrollTo(0,0)')
        #     res = self.__handle_widget()
        #     # 目前只处理一次刷新，执行报错后修改flag标识
        #     if self._taskExecution._newWindow:
        #         self._taskExecution._newWindow = False
        except StopSetCycle:
            raise StopSetCycle()
        except Exception as e:
            # 强制执行
            error_log = self._currentWidget.get("error_log") if self._currentWidget.get("error_log") else ""
            if error_log:
                self._taskExecution._execute_error_last = error_log
            force_execute = self._currentWidget.get("force_execute")
            if not force_execute:
                # 非强制执行 记录日志且抛错终止执行
                if error_log:
                    self._taskExecution._exceptionTag = False
                self._taskExecution._log_business = self._taskExecution._log_business + error_log + "<br/>"
                raise e
            res = False


        # 关闭alert弹窗
        if res:
            self.__closeAlert()

        # 页面自己关闭浏览器
        self.__closeWindowSelf()

        # 人工判断关闭浏览器
        self.__closeWindowActive()

        # 打开新浏览器窗口
        if res:
            self.__openNewBrowser()

        # 下一步骤
        self.__widgetEntryNextStep()

    # 采集alert弹窗
    def __collectAlertValue(self):
        # 弹窗内容
        # 弹窗标识  TODO
        isAlert = self._currentWidget.get('is_alert')  # 是否alert弹窗
        actionType = self._currentWidget.get('action_type')
        if isAlert and actionType != '13':
            alert = WebDriverWait(self._driver, 1000, 0.1).until(EC.alert_is_present())
            # 弹窗文本
            alert_text = alert.text
            self._taskExecution._log = self._taskExecution._log + alert_text + "<br/>"
            self._taskExecution._log_business = self._taskExecution._log_business + alert_text + "<br/>"
            self.__setBrowserValue(alert_text)
            print('ALERT采集到的内容：', self._taskExecution._widgetValues)
        else:
            pass

    # 延迟等待
    def __widgetDelay(self):
        delay = self._currentWidget.get('delay')
        print('delay=', delay)
        if delay:
            time.sleep(float(delay))
        else:
            pass

    # 切换采集元素iframe窗口
    def __switchCollectIframe(self, timeout=ExecTimeout):
        self._stepExecution.switchIframe(self._currentWidget.get('collect_iframe'), timeout)

    # 切换动作iframe窗口
    def __switchActionIframe(self, timeout=ExecTimeout):
        self._stepExecution.switchIframe(self._currentWidget.get('action_iframe'), timeout)

    # 处理每个控件的执行情况
    def __handle_widget(self):
        # 超时时间
        timeout = self._currentWidget.get('timeout')
        if timeout:
            timeout = int(timeout)
        else:
            timeout = ExecTimeout
        timeout = timeout if timeout > 0 else ExecTimeout
        self._currentWidget["timeout"] = timeout

        # 页面元素采集
        self.__collectBrowserValue()

        # 集循环条件判断
        if self._currentWidget.get("has_set_cycle_conditions"):
            set_cycle_conditions = self._widgetSetExecution._getSetConditionFilter()
            if len(set_cycle_conditions):
                if not self._taskExecution._conditionFilter(set_cycle_conditions,
                                                            self._widgetSetExecution._currentWidgetSet):
                    raise StopSetCycle()

        # 控件执行条件
        if not self._taskExecution._conditionFilter(self.__getConditionFilter(),
                                                    self._widgetSetExecution._currentWidgetSet):
            print('控件名称：', self._currentWidget.get('action_name'), '，不满足条件...')
            return False

        # 执行动作控件
        self.__handleActionWidget()

        # 采集弹窗的值
        self.__collectAlertValue()

        return True

    def __getFullXpath(self, current_xpath, input_value):
        if (not current_xpath.startswith("./")) and (not current_xpath.startswith('../')):
            if isinstance(input_value, str):
                current_xpath = current_xpath.replace("{var}", input_value)
            return current_xpath

        if current_xpath.startswith('../'):
            current_xpath = "%s%s" % (r"//", current_xpath)

        widget_set = self._widgetSetExecution._currentWidgetSet  # 当前控件集
        parent_xpath = widget_set.get('parent_xpath')
        if parent_xpath:
            child_path = "" if current_xpath == "./" else current_xpath[1:]
            current_xpath = parent_xpath + '[' + str(
                int(self._widgetSetExecution._currentWidgetSet.get('element_idx')) + 1) + ']' + child_path

        if isinstance(input_value, str):
            current_xpath = current_xpath.replace("{var}", input_value)
        return current_xpath

    def __handleActionWidget(self):
        # 判断是否输入或下拉选择动作，是则找出INPUT的内容,取第一条，数据有且只有一条
        inputValue = self.__getInputConditionValue()
        self._taskExecution._log = self._taskExecution._log + "输入值：" + inputValue + "<br/>"
        # 动作类型ACTION_TYPE
        actionType = self._currentWidget.get('action_type')
        # 定位XPATH
        xpath = self._currentWidget.get('action_xpath')
        element = None
        if xpath:
            # 定位元素，等待根据xpath定位的元素出现在DOM中，是可见的，并且宽高都大于0，一旦可见则返回WebElement
            self.__switchActionIframe(self._currentWidget.get('timeout'))
            xpath = self.__getFullXpath(xpath, inputValue)
            # try:
            #     element = WebDriverWait(self._driver, self._currentWidget.get('timeout'), 0.1).until(
            #         EC.visibility_of_element_located((By.XPATH, xpath)))
            # except Exception as e:
            #     if self._taskExecution._newWindow:
            #         raise FirstWidgetTimeoutException()
            #     else:
            #         raise e
            element = WebDriverWait(self._driver, self._currentWidget.get('timeout'), 0.1).until(
                EC.visibility_of_element_located((By.XPATH, xpath)))
        if not actionType:
            return

        if actionType == '1':
            # 悬浮
            ActionChains(self._driver).move_to_element(element).perform()
        elif actionType == '2' or actionType == '7' or actionType == '8':
            # 点击事件  目前 单选及复选 通用 点击事件
            # 获取重复次数
            repetition_frequency = self._currentWidget.get('repetition_frequency')
            if repetition_frequency:
                count = int(repetition_frequency)
                for v in range(0, count):
                    print('控件：', self._currentWidget.get('action_name'), '点击了')
                    time.sleep(1)
                    # ActionChains(self._driver).move_to_element(element).click(element).perform()
                    element.click()
            else:
                # ActionChains(self._driver).move_to_element(element).click(element).perform()
                # self._driver.execute_script("arguments[0].click();",element)
                element.click()
                if actionType == '7' or actionType == '8':
                    flag = True
                    while flag:
                        flag = element.is_selected()
                        if flag:
                            flag = False
                        else:
                            element.click()
                        print('复选进行中....')

            print('控件：', self._currentWidget.get('control_name'), '进行了点击事件..............')
        elif actionType == "210":
            ActionChains(self._driver).move_to_element(element).click(element).perform()
        elif actionType == '3':
            # 双击事件
            ActionChains(self._driver).move_to_element(element).double_click(element).perform()
        elif actionType == '4':
            # 滚屏
            self._driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            self._driver.execute_script('window.scrollTo(0,0)')
        elif actionType == '5':
            # 判断是否有readOnly属性,且有id
            attrFlag = element.get_attribute('readOnly')
            idFlag = element.get_attribute('id')
            if attrFlag and idFlag:
                # 截取ID属性  TODO
                sId = xpath.replace(" ", "")
                elId = sId[sId.rindex("id=") + 4:sId.rindex("]") - 1]
                js = "document.getElementById('" + elId + "').removeAttribute('readOnly');"
                self._driver.execute_script(js)
                time.sleep(2)
            # 输入
            element.clear()
            element.send_keys(inputValue)
        elif actionType == '6':
            # 下拉选择
            typer = 'text'
            selector = Select(element)
            if typer == 'text':
                selector.select_by_visible_text(inputValue)
            elif typer == 'value':
                selector.select_by_value(inputValue)
            else:
                selector.select_by_index(inputValue)
            print('下拉选结束...')
        elif actionType == '9':
            # =其他
            pass
        elif actionType == '10':
            # =返回
            self._driver.back()
        elif actionType == '11':
            # =提交
            element.click()
        elif actionType == '12':
            # 等待控件消失
            WebDriverWait(self._driver, 60, 0.1).until_not(EC.visibility_of_element_located((By.XPATH, xpath)))
        elif actionType == '13':
            # 弹窗处理
            alert = WebDriverWait(self._driver, 20, 0.1).until(EC.alert_is_present())
            alert_text = alert.text
            self._taskExecution._log = self._taskExecution._log + alert_text + "<br/>"
            self._taskExecution._log_business = self._taskExecution._log_business + alert_text + "<br/>"
            self.__setBrowserValue(alert_text)
            alert.accept()  # 点击确定
        elif actionType == '14':
            # 特殊动作
            action_code = self._currentWidget.get('action_code')
            data_source = self._taskExecution._widgetValues if self._taskExecution._widgetValues else {}
            # 内存数据（采集数据）
            collect_data = execute_document.collect_data_to_data_format(
                data_source) if "collect_data" in action_code else "${None}"
            # 执行列表数据
            document_data = "${None}"
            if "document_data" in action_code:
                params = {
                    "data_type": "1",
                    "task_id": self._currentWidget.get("task_id"),
                    "ids": [self._taskExecution._resource.get("key")]
                }
                zn, document_data = datatableservice.find_table_value_by_group_id(params)
                document_data = document_data[0]
                extra_data = self._taskExecution._resource.get("document_data")
                for edk, edv in extra_data.items():
                    document_data[edk] = edv
            con = {'inputValue': inputValue, 'currentWidget': self._currentWidget, 'self_': self,
                   "collect_data": json.dumps(collect_data),
                   "document_data": json.dumps(document_data)}
            exec(action_code, con)
            params = con["get_execute_params"]()  # json格式数据
            if params.get('$this'):
                params['$this'] = action_code  # 用于将自己作为参数
            # 参数校验
            for param_k, param_v in params.items():
                if not param_v:
                    params[param_k] = "${None}"
            data = json.dumps(params)
            path = '/session/' + self._driver.session_id + '/exeCmd'
            url = '%s%s' % (self._driver.command_executor._url, path)
            result = self._driver.command_executor._request('POST', url, body=data.encode("utf-8"))
            if result.get('status') == 55:
                raise Exception(result.get('value'))
        elif actionType == '15':
            # 鼠标滚动
            self._driver.execute_script('arguments[0].scrollIntoView();', element)
        elif actionType == '16':
            # 判断控件是否要执行自定义代码
            actionCode = self._currentWidget.get('action_code')
            data_source = self._taskExecution._widgetValues if self._taskExecution._widgetValues else {}
            # 内存数据（采集数据）
            collect_data = execute_document.collect_data_to_data_format(
                data_source) if "collect_data" in actionCode else "${None}"
            # 执行列表数据
            document_data = "${None}"
            if "document_data" in actionCode:
                params = {
                    "data_type": "1",
                    "task_id": self._currentWidget.get("task_id"),
                    "ids": [self._taskExecution._resource.get("key")]
                }
                zn, document_data = datatableservice.find_table_value_by_group_id(params)
                document_data = document_data[0]
                extra_data = self._taskExecution._resource.get("document_data")
                for edk, edv in extra_data.items():
                    document_data[edk] = edv
            json_ = {"driver": self._driver, 'inputValue': inputValue, "self_": self,
                     "currentWidget": self._currentWidget,
                     "collect_data": collect_data,
                     "document_data": document_data}
            exec(actionCode, json_)
            browser_value = json_['main']()
            if browser_value:
                self.__setBrowserValue(browser_value)
        elif actionType == '888':
            # 文书内容替换--冻结用到
            self.replaceDoc(inputValue)
        elif actionType == '999':
            # 打印指令
            self.__printPDF()
        elif actionType == '2998':
            # 文书生成-第一版
            action_code = self._currentWidget.get('action_code')
            if not ("main_server" in action_code):
                raise Exception("动作代码缺少main_server方法")
            if not ("main_client" in action_code):
                raise Exception("动作代码缺少main_client方法")
            if not inputValue:
                raise Exception("文书生成缺少必要参数")

            document_param_array = re.findall("\${(.*?)}", inputValue)
            if len(document_param_array) < 1:
                raise Exception("文书生成参数格式不正确")

            for document_param in document_param_array:
                var_value = var_service.get_var_by_var_name(document_param)
                var_value = var_value.get("var_value_data")
                if var_value:
                    var_value = var_value.get("var_value")
                    if not var_value:
                        var_value = ""
                    inputValue = inputValue.replace("${" + document_param + "}", var_value)
                else:
                    inputValue = inputValue.replace("${" + document_param + "}", "")

            inputValue = inputValue.replace("\\", "/").replace("\u202a", "").replace("\u202A", "")
            data_source = self._taskExecution._widgetValues
            data_dealt = execute_document.collect_data_to_data_format(data_source)

            # 服务端自定义执行
            # 暂无

            # document(inputValue, data_dealt, self._taskExecution._resource.get("document_data"))
            # 客户端自定义执行
            params = {
                'p1': 'C:/seleniumNode/Python36/pythonw.exe',
                'p2': 'C:/upload/runtime_handle.py',
                'p3': 'main_client',
                '$this': action_code,
                'p4': inputValue,
                'p5': json.dumps(data_dealt),
                'p6': json.dumps(self._taskExecution._resource.get("document_data"))
            }
            data = json.dumps(params)
            path = '/session/' + self._driver.session_id + '/exeCmd'
            url = '%s%s' % (self._driver.command_executor._url, path)
            result = self._driver.command_executor._request('POST', url, body=data.encode("utf-8"))
            if result.get('status') == 55 or result.get('status') == 500:
                raise Exception(result.get('value'))
        elif actionType == '1998':
            # 文书生成(新)
            action_code = self._currentWidget.get('action_code')
            if not ("main_server" in action_code):
                raise Exception("动作代码缺少main_server方法")
            if not ("main_client" in action_code):
                raise Exception("动作代码缺少main_client方法")
            if not inputValue:
                raise Exception("文书生成缺少必要参数")

            document_param_array = re.findall("\${(.*?)}", inputValue)
            if len(document_param_array) < 1:
                raise Exception("文书生成参数格式不正确")

            for document_param in document_param_array:
                var_value = var_service.get_var_by_var_name(document_param)
                var_value = var_value.get("var_value_data")
                if var_value:
                    var_value = var_value.get("var_value")
                    if not var_value:
                        var_value = ""
                    inputValue = inputValue.replace("${" + document_param + "}", var_value)
                else:
                    inputValue = inputValue.replace("${" + document_param + "}", "")

            # 服务端自定义执行
            # 暂无

            # document_new(inputValue, self._taskExecution._resource)
            # 客户端自定义执行
            params = {
                'p1': 'C:/seleniumNode/Python36/pythonw.exe',
                'p2': 'C:/upload/runtime_handle.py',
                # 'p2': 'D:/svn/clever-spiders/trunk/clever-spiders/service/client/runtime_handle.py',
                'p3': 'main_client',
                '$this': action_code,
                'p4': inputValue,
                'p5': json.dumps(self._taskExecution._resource)
            }
            data = json.dumps(params)
            path = '/session/' + self._driver.session_id + '/exeCmd'
            url = '%s%s' % (self._driver.command_executor._url, path)
            result = self._driver.command_executor._request('POST', url, body=data.encode("utf-8"))
            if result.get('status') == 55 or result.get('status') == 500:
                raise Exception(result.get('value'))
        elif actionType == '998':
            # 文书生成-第三版
            action_code = self._currentWidget.get('action_code')
            if not ("main_server" in action_code):
                raise Exception("动作代码缺少main_server方法")
            if not ("main_client" in action_code):
                raise Exception("动作代码缺少main_client方法")
            if not inputValue:
                raise Exception("文书生成缺少必要参数")

            document_param_array = re.findall("\${(.*?)}", inputValue)
            if len(document_param_array) < 1:
                raise Exception("文书生成参数格式不正确")

            for document_param in document_param_array:
                var_value = var_service.get_var_by_var_name(document_param)
                var_value = var_value.get("var_value_data")
                if var_value:
                    var_value = var_value.get("var_value")
                    if not var_value:
                        var_value = ""
                    inputValue = inputValue.replace("${" + document_param + "}", var_value)
                else:
                    inputValue = inputValue.replace("${" + document_param + "}", "")
            inputValue = inputValue.replace("\\", "/").replace("\u202a", "").replace("\u202A", "")
            data_source = self._taskExecution._widgetValues
            data_dealt = execute_document.collect_data_to_data_format(data_source)
            data_dealt_str = json.dumps(data_dealt) if data_dealt else "${None}"
            # document_third(inputValue, self._currentWidget.get("task_id"), self._taskExecution._resource,
            #                ":".join([ConfigHelper.HOST_IP, str(ConfigHelper.HOST_PORT)]), self._taskExecution._batchParam, data_dealt)
            params = {
                'p1': 'C:/seleniumNode/Python36/pythonw.exe',
                'p2': 'C:/upload/runtime_handle.py',
                'p3': 'main_client',
                '$this': action_code,
                'p4': inputValue,
                'p5': self._currentWidget.get("task_id"),
                "p6": json.dumps(self._taskExecution._resource),
                'p7': ":".join([ConfigHelper.HOST_IP, str(ConfigHelper.HOST_PORT)]),
                'p8': json.dumps(self._taskExecution._batchParam),
                'p9': data_dealt_str
            }
            # 参数校验
            for param_k, param_v in params.items():
                if not param_v:
                    params[param_k] = "${None}"
            data = json.dumps(params)
            path = '/session/' + self._driver.session_id + '/exeCmd'
            url = '%s%s' % (self._driver.command_executor._url, path)
            result = self._driver.command_executor._request('POST', url, body=data.encode("utf-8"))
            if result.get('status') == 55 or result.get('status') == 500:
                raise Exception(result.get('value'))
            else:
                self._taskExecution._log = self._taskExecution._log + result.get('value') + "<br/>"
        elif actionType == '4000':
            self.__xiangan_qianzhang_print()
        elif actionType == '4001':
            self.__xiangan_new_caiding(inputValue)
        elif actionType == '4002':
            self.__wenshushangchuan(inputValue)
        elif actionType == '4003':
            self.__yinrufalvwenshu(inputValue)
        elif actionType == '007':   # 模态窗口JS点击
            # js = 'document.getElementsByTagName("input")[0]'     # TODO 前端传入
            js = self._currentWidget.get('js_position_expression')
            print('JS进行了点击.....js代码：' + js)
            if js:
                self._driver.execute_script('setTimeout(function(){'+ js + '.click()},100)')
        else:
            pass

    # 翔安签章打印
    def __xiangan_qianzhang_print(self):

        path = '/session/' + self._driver.session_id + '/exeCmd'
        url = '%s%s' % (self._driver.command_executor._url, path)
        data = '{"p1":"C:/upload/win_ctrl.exe","p2":"%s"}' % ('xiangan_qz_print()')
        result = self._driver.command_executor._request('POST', url, body=data.encode("utf-8"))
        if result.get('status') == 55:
            raise Exception(result.get('value'))
        time.sleep(4)
        # 打印完成后关闭PDF文件窗口
        self.__closeWindowActive_print()
        print('打印窗口关闭后：', self._taskExecution._openedWindows)

    # 翔安新增裁定书替换
    def __xiangan_new_caiding(self, inputValue):
        path = '/session/' + self._driver.session_id + '/exeCmd'
        url = '%s%s' % (self._driver.command_executor._url, path)
        x = r"filename='" + inputValue + "'"
        y = 'xiangan_xinzengcaidingshu'
        data = '{"p1":"C:/upload/win_ctrl.exe","p2":"xiangan_xinzengcaidingshu","p3":"' + x + '"}'
        result = self._driver.command_executor._request('POST', url, body=data.encode("utf-8"))
        if result.get('status') == 55:
            raise Exception(result.get('value'))
        time.sleep(2)

    # 思明批量文书上传功能
    def __wenshushangchuan(self, inputValue):
        path = '/session/' + self._driver.session_id + '/exeCmd'
        url = '%s%s' % (self._driver.command_executor._url, path)
        x = r"file_dir='" + inputValue + "',filenames=''"
        # y = 'wenshushangchuan'
        data = '{"p1":"C:/upload/win_ctrl.exe","p2":"wenshushangchuan","p3":"' + x + '"}'
        # data = '{"p1":"C:/upload/win_ctrl.exe","p2":"%s","p3":"%s"}' % ('xiangan_xinzengcaidingshu()', inputValue)
        result = self._driver.command_executor._request('POST', url, body=data.encode("utf-8"))
        if result.get('status') == 55:
            raise Exception(result.get('value'))
        time.sleep(2)

    # 思明保全引入法律文书
    def __yinrufalvwenshu(self, inputValue):
        path = '/session/' + self._driver.session_id + '/exeCmd'
        url = '%s%s' % (self._driver.command_executor._url, path)
        x = r"filenames='" + inputValue + "'"
        # y = 'baoquan_yinru_falvwenshu'
        data = '{"p1":"C:/upload/win_ctrl.exe","p2":"baoquan_yinru_falvwenshu","p3":"' + x + '"}'
        # data = '{"p1":"C:/upload/win_ctrl.exe","p2":"%s","p3":"%s"}' % ('xiangan_xinzengcaidingshu()', inputValue)
        result = self._driver.command_executor._request('POST', url, body=data.encode("utf-8"))
        if result.get('status') == 55:
            raise Exception(result.get('value'))
        time.sleep(2)

    # 文书生成方法
    def __createDocumentZN(self, inputValue, fill_datas):
        if not inputValue:
            raise Exception("文书生成缺少必要参数")

        document_param_array = re.findall("\${(.*?)}", inputValue)
        if len(document_param_array) < 1:
            raise Exception("文书生成参数格式不正确")

        for document_param in document_param_array:
            var_value = var_service.get_var_by_var_name(document_param)
            var_value = var_value.get("var_value_data")
            if var_value:
                var_value = var_value.get("var_value")
                if not var_value:
                    var_value = ""
                inputValue = inputValue.replace("${" + document_param + "}", var_value)
            else:
                inputValue = inputValue.replace("${" + document_param + "}", "")

        data_source = self._taskExecution._widgetValues
        data_format = execute_document.collect_data_to_data_format(data_source)

        # print("main_datas:", main_datas)
        # document(inputValue, data)
        main_datas = {}
        fill_datas = {}
        # 读取指定文件夹下目录
        main_datas = json.dumps(main_datas, ensure_ascii=False).replace('"', '\\"')
        fill_datas = json.dumps(fill_datas, ensure_ascii=False).replace('"', '\\"')
        path = '/session/' + self._driver.session_id + '/exeCmd'
        url = '%s%s' % (self._driver.command_executor._url, path)
        data = '{"p1": "C:/upload/document_create.exe","p2":"%s","p3":"%s","p4":"%s"}' % (
            inputValue, main_datas, fill_datas)
        result = self._driver.command_executor._request('POST', url, body=data.encode("utf-8"))
        if result.get('status') == 55:
            raise Exception(result.get('value'))

    # TODO 打印方法
    def __printPDF(self):
        id1 = self._widgetSetExecution._currentWidgetSet.get('widget_set_name')
        id2 = self._currentWidget.get('control_name')
        pdf_url = self._taskExecution._widgetValues.get(id1).get(id2).get('0').get('0')
        print('PDF文件下载路径：', pdf_url)
        if pdf_url:
            # 打开PDF文件新窗口
            self._driver.execute_script(r"window.open('" + pdf_url + "')")
            # 采集打开窗口
            self.__openNewBrowser_print()
            # 置顶
            # self.__stickWindow()

            path = '/session/' + self._driver.session_id + '/exeCmd'
            url = '%s%s' % (self._driver.command_executor._url, path)
            data = """{"p1": "C:\seleniumNode\Python36\pythonw.exe", "p2": "main", "p3": '''
def main():
    from utils.win_ctrl import win32
    import time
    time.sleep(1)
    win32.combination_key("ctrl+p")
    x = win32.win_wait(title='打印', classname='#32770')
    time.sleep(1)
    y = win32.win_wait(x[0], classname='Button', instance=49)
    win32._win_click(y[0])
    '''}"""
            result = self._driver.command_executor._request('POST', url, body=data.encode("utf-8"))
            if result.get('status') == 55:
                raise Exception(result.get('value'))
            time.sleep(4)

            # 打印完成后关闭PDF文件窗口
            self.__closeWindowActive_print()
            print('打印窗口关闭后：', self._taskExecution._openedWindows)

    def __stickWindow(self):
        title = self._driver.title + " - Internet Explorer"
        hdnd = win32gui.FindWindow('IEFrame', title)
        if hdnd:
            win32gui.SetForegroundWindow(hdnd)
            print('置顶窗口==================', title)

    # 关闭alert弹窗
    def __closeAlert(self):
        # 弹窗标识
        isAlert = self._currentWidget.get('is_alert')  # 是否alert弹窗
        closeAlertType = self._currentWidget.get('close_alert')  # 是否关闭alert弹窗 NO_CLOSE  CLOSE_ACCEPT  CLOSE_DISMISS
        actionType = self._currentWidget.get('action_type')
        print('isAlert：', isAlert, 'isCloseAlert：', closeAlertType)
        if isAlert and actionType != '13':
            alert = WebDriverWait(self._driver, 1000, 0.1).until(EC.alert_is_present())
            if closeAlertType == 'CLOSE_ACCEPT':
                # 确定
                alert.accept()
                print('alert弹窗确定')
            elif closeAlertType == 'CLOSE_DISMISS':
                # 取消
                alert.dismiss()
                print('alert弹窗取消')
            else:
                pass
            time.sleep(1.5)
            print('alert关闭方式：', closeAlertType)
        else:
            pass

    # 自身关闭浏览器
    def __closeWindowSelf(self):
        # 判断操作自身是否关闭浏览器
        if self._currentWidget.get('close_window_self'):
            while True:
                starttime = time.time()
                if len(self._driver.window_handles) < len(
                        self._taskExecution._openedWindows) or time.time() - starttime > ExecTimeout:
                    break
            # 最后一个窗口句柄出队
            popWindow = self._taskExecution._openedWindows.pop(-1)
            self._taskExecution._windowsData.pop(popWindow)

            self._taskExecution._currentWindow = self._taskExecution._openedWindows[-1]  # 表示从右往左开始
            self._driver.switch_to.window(self._taskExecution._currentWindow)
            self._taskExecution._windowsData[self._taskExecution._currentWindow] = {'iframe': ''}

    # 人为关闭浏览器
    def __closeWindowActive(self):
        # 判断是否人为的关闭浏览器
        if self._currentWidget.get('close_window_active'):
            if self._currentWidget.get('close_window_active_type') == '1':  # 默认关闭窗口
                self._driver.close()
            else:  # js关闭窗口
                self._driver.execute_script("window.opener=null")  # 屏蔽关闭窗口提示
                self._driver.execute_script("window.close()")  # 关闭窗口

            # 最后一个窗口句柄出队
            popWindow = self._taskExecution._openedWindows.pop(-1)
            self._taskExecution._windowsData.pop(popWindow)

            self._taskExecution._currentWindow = self._taskExecution._openedWindows[-1]  # 表示从右往左开始
            self._driver.switch_to.window(self._taskExecution._currentWindow)
            self._taskExecution._windowsData[self._taskExecution._currentWindow] = {
                'iframe': ''}  # 关闭窗口切换回原页面时，以前切换的iframe被清空

    # 人为关闭浏览器
    def __closeWindowActive_print(self):
        # 判断是否人为的关闭浏览器
        # self._driver.execute_script("window.opener=null")  # 屏蔽关闭窗口提示
        # self._driver.execute_script("window.close()")  # 关闭窗口
        self._driver.close()
        # 最后一个窗口句柄出队
        popWindow = self._taskExecution._openedWindows.pop(-1)
        self._taskExecution._windowsData.pop(popWindow)

        self._taskExecution._currentWindow = self._taskExecution._openedWindows[-1]  # 表示从右往左开始
        self._driver.switch_to.window(self._taskExecution._currentWindow)
        self._taskExecution._windowsData[self._taskExecution._currentWindow] = {
            'iframe': ''}  # 关闭窗口切换回原页面时，以前切换的iframe被清空

    # 打开新浏览器窗口，切换窗口并追加窗口到数组__openedWindows
    def __openNewBrowser(self):
        # 判断是否有打开新浏览器窗口
        if self._currentWidget.get('open_new_browser'):
            starttime = time.time()
            while True:
                print('等待新窗口打开===================================')
                if len(self._driver.window_handles) > len(
                        self._taskExecution._openedWindows) or time.time() - starttime > ExecTimeout:
                    break

            wins = self._driver.window_handles
            print(wins)
            for win in wins:
                if win in self._taskExecution._openedWindows:
                    pass
                else:
                    self._driver.switch_to.window(win)
                    self._taskExecution._currentWindow = win
                    self._taskExecution._openedWindows.append(win)
                    self._taskExecution._windowsData[self._taskExecution._currentWindow] = {'iframe': ''}
                    # 标记新窗口flag
                    self._taskExecution._newWindow = True
                    # 滚动窗口
                    if self._currentWidget.get('window_size') == '0':
                        self._driver.maximize_window()
                    self._driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                    self._driver.execute_script('window.scrollTo(0,0)')
                    print('_windowsData=========', self._taskExecution._windowsData)

    # 打开新浏览器窗口，切换窗口并追加窗口到数组__openedWindows
    def __openNewBrowser_print(self):
        # 判断是否有打开新浏览器窗口
        while True:
            starttime = time.time()
            print('等待新窗口打开===================================')
            if len(self._driver.window_handles) > len(
                    self._taskExecution._openedWindows) or time.time() - starttime > ExecTimeout:
                break

        wins = self._driver.window_handles
        print(wins)
        for win in wins:
            if win in self._taskExecution._openedWindows:
                pass
            else:
                self._driver.switch_to.window(win)
                self._taskExecution._currentWindow = win
                self._taskExecution._openedWindows.append(win)
                self._taskExecution._windowsData[self._taskExecution._currentWindow] = {'iframe': ''}
                # 滚动窗口
                if self._currentWidget.get('window_size') == '0':
                    self._driver.maximize_window()

    # 下一步骤，查看是否有指向进入下一步骤，无则跳过
    def __widgetEntryNextStep(self):

        # 从条件值中获取下一步骤
        nextConditions = self.__getCondictionNext()
        # 判断跳转条件个数
        if len(nextConditions) > 0:
            condition_null = None
            for nextCondition in nextConditions:
                widgetId = nextCondition.get('widget_id_left')
                leftValue = nextCondition.get('value_left')
                leftValueTemporary = nextCondition.get('value_temporary_left')
                if not widgetId and not leftValue and not leftValueTemporary:  # 三种条件都没有则为无条件跳转
                    condition_null = nextCondition
                    break
            if condition_null:
                nextStep = self._stepExecution.getNextStep(condition_null.get('enter_next_id'))
                stepExecution = StepExecution(self._taskExecution, nextStep, self)
                stepExecution.executeStep()
                print('无条件跳转...........................')
            else:
                # 下一步骤ID
                enrer_next_id = ''
                next_condition_result = {}  # {下一步骤id: 条件值数组}
                next_condition_step = {}  # {下一步骤id: 逻辑表达式}

                # 流转条件结果结算并按照下一步骤id归类
                for nextCondition_ in nextConditions:
                    # 获取比较左右比较内容比较返回结果
                    flag = self._taskExecution._getCompareRes(nextCondition_,
                                                              self._widgetSetExecution._currentWidgetSet)

                    next_step_id = nextCondition_.get("enter_next_id")

                    if next_step_id in next_condition_result:
                        temp = next_condition_result.get(next_step_id)
                        temp[nextCondition_.get("group")] = flag.__str__()
                    else:
                        next_condition_result[next_step_id] = {nextCondition_.get("group"): flag.__str__()}

                    if not next_step_id in next_condition_step:
                        next_condition_step[next_step_id] = nextCondition_.get("logical_expression")

                # 根据判断结果决定下一步骤
                flag = False
                for k, v in next_condition_step.items():
                    logical_expression = v
                    condition_dict = next_condition_result.get(k)
                    for k_, v_ in condition_dict.items():
                        logical_expression = logical_expression.replace(k_, v_)
                    if logical_expression:
                        flag = eval(logical_expression)
                        if flag:
                            enrer_next_id = k
                            if enrer_next_id:
                                nextStep = self._stepExecution.getNextStep(enrer_next_id)
                                stepExecution = StepExecution(self._taskExecution, nextStep, self)
                                stepExecution.executeStep()
                            else:
                                pass

        else:  # 无next条件
            pass

    # 获取进入下一步骤条件
    def __getCondictionNext(self):
        conditionValues = self._currentWidget.get('condition_values')
        print(conditionValues)
        # 根据控件ID查询所有条件值FILTER的值
        # filter_conditions = find_condition_values_by_widget_id(widgetId,'FILTER')
        filter_conditions = []
        if conditionValues:
            for conditionValue in conditionValues:
                if conditionValue.get('condition_type') == 'NEXT':
                    filter_conditions.append(conditionValue)
        return filter_conditions

    # 获取条件值
    def __getInputConditionValue(self):
        # 获取条件值
        condition_values = self._currentWidget.get('condition_values')
        if condition_values:
            input_condition = None
            for condition_value in condition_values:
                if condition_value.get('condition_type') == 'INPUT':
                    input_condition = condition_value
                    break
            if input_condition:
                resValue = ''
                # 判断输入内容值是来自外部数据源还是具体值
                outerKey = input_condition.get('value_temporary_right')
                if outerKey:
                    resValue = self._taskExecution._getResourceValue(outerKey)
                else:
                    pageIndex = self._widgetSetExecution._currentWidgetSet.get('turn_page_index')
                    rowIndex = self._widgetSetExecution._currentWidgetSet.get('row_index')
                    resValue = self._taskExecution._getWidgetValue(input_condition, pageIndex, rowIndex)
                resValue = resValue if resValue else input_condition.get('value_right')

                if resValue:
                    # 判断是否有数据处理表达式
                    if input_condition.get('logical_expression'):   # todo 借用字段 - logical_expression 动作表达式
                        temp = input_condition.get('logical_expression')
                        if temp.startswith(r're'):
                            temp = temp.replace(r'$', "'" + resValue + "'")
                            resValue = eval(temp)
                        else:
                            # 判断是否存在数据类型 默认 TEXT
                            input_data_type = input_condition.get('input_data_type')
                            if not input_data_type:
                                input_data_type = 'TEXT'
                            if input_data_type == 'TEXT':
                                temp = temp.replace(r'$',resValue)
                                resValue = temp
                            elif input_data_type == 'NUMBER':
                                temp = temp.replace(r'$', str(resValue))
                                resValue = eval(temp)
                return str(resValue)
            return ''
        return ''

    # 采集页面元素
    def __collectBrowserValue(self):
        # 获取需要xpath找到页面的内容
        collect_xpath = self._currentWidget.get('collect_xpath')  # 标识 - XPATH，获取这个位置的内容用于对比
        # 获取标识类型(根据标识类型判断是获取页面元素的text还是value等属性的值)
        collect_type = self._currentWidget.get('collect_type')
        if not collect_xpath or not collect_type:
            return

        # 获取标识的内容（指定VALUE则获取value属性的值，默认获取text） -- 暂时这样处理 TODO
        try:
            self.__switchCollectIframe(self._currentWidget.get('timeout'))
        except SwitchIframeCycle:
            return

        xpath = self.__getFullXpath(collect_xpath, None)
        element = WebDriverWait(self._driver, self._currentWidget.get('timeout'), 0.1).until(EC.visibility_of_element_located((By.XPATH, xpath)))

        # 采集到的页面值
        browser_value = element.get_attribute(collect_type).strip()  # 修改存储格式，传入需要采集的类型，前端入库设置，字典设置类型 TODO
        # 获取值类型
        collect_value_type = self._currentWidget.get('collect_value_type')
        # 获取值格式
        collect_value_format = self._currentWidget.get('collect_value_format')
        if collect_value_type == 'DATE' and collect_value_format and browser_value:  # 日期格式转换为时间戳
            timeArray = time.strptime(browser_value, collect_value_format)
            browser_value = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

        self.__setBrowserValue(browser_value)

    def __setBrowserValue(self, browser_value):
        # 控件集id
        widgetsetname = self._widgetSetExecution._currentWidgetSet.get("widget_set_name")
        pageValues = self._taskExecution._widgetValues.get(widgetsetname)  # 分页数组
        if not pageValues:
            pageValues = {}
            self._taskExecution._widgetValues[widgetsetname] = pageValues
        # 控件id
        controlname = self._currentWidget.get('control_name')
        widgetValues = pageValues.get(controlname)  # 分页数组
        if not widgetValues:
            widgetValues = {}
            pageValues[controlname] = widgetValues
        turn_page_index = self._widgetSetExecution._currentWidgetSet.get('turn_page_index')  # 分页索引
        browserValues = widgetValues.get(turn_page_index)  # 页面数组
        if not browserValues:
            browserValues = {}
            widgetValues[turn_page_index] = browserValues
        element_idx = self._widgetSetExecution._currentWidgetSet.get('element_idx')  # 页面索引
        browserValues[element_idx] = browser_value
        print('采集值：=================', self._taskExecution._widgetValues)

    # 获取FILTER的条件值
    def __getConditionFilter(self):
        conditionValues = self._currentWidget.get('condition_values')
        filter_conditions = []
        if conditionValues:
            for conditionValue in conditionValues:
                if conditionValue.get('condition_type') == 'FILTER':
                    filter_conditions.append(conditionValue)
        return filter_conditions

    # 文书替换
    def replaceDoc(self, inputValue):
        # pythoncom.CoInitialize()
        path = '/session/' + self._driver.session_id + '/exeCmd'
        url = '%s%s' % (self._driver.command_executor._url, path)
        data = '{"p1":"C:/upload/runtime_handle.exe","p2":"%s","p3":"%s"}' % (
            'document_replace()', inputValue.replace('\\', '/'))
        result = self._driver.command_executor._request('POST', url, body=data.encode("utf-8"))
        if result.get('status') == 55:
            raise Exception(result.get('value'))
