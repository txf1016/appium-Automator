# coding:utf8

from appium import webdriver
from time import sleep
from enum import Enum
import pathConf
from desConf import DesConf

'''
    使用appium1.5版本以上
'''


class CommonTools:
    remoteHost = 'http://127.0.0.1:4723/wd/hub'

    def __init__(self):
        self._driver = None
        self.androidDes = DesConf().android_Des
        self.androidDes['app'] = pathConf.app_name_path

    def init_Driver(self):
        # DesConf.android_Des['app'] = pathConf.app_name_path
        #  # 'app': PATH('//Users/tanxiaofen/Downloads/inface.zip') IOS
        # print DesConf.android_Des
        self._driver = webdriver.Remote(self.remoteHost, self.androidDes)

    def quit_Driver(self):
        if self._driver:
            self._driver.quit()

    """
   给定控件的xpatch, id 或者name来查找控件

   :Args:
        - controlInfo: 控件的信息，可以是xpath,id或者其他属性

   :Return:
       如果找到控件，返回第一个

   :Usage:
       self.findElement(controlInfo)
   """

    # 定位元素
    def findElement(self, controlInfo):
        if controlInfo.startswith("//"):
            element = self._driver.find_element_by_xpath(controlInfo)
        elif ":id/" in controlInfo or ":string/" in controlInfo:
            element = self._driver.find_element_by_id(controlInfo)
        else:
            element = self._driver.find_element_by_class_name(controlInfo)
        return element

    """
    给定控件的xpatch, id 或者name来查找控件

    :Args:
         - controlInfo: 控件的信息，可以是xpath,id或者其他属性

    :Return:
        返回所有满足条件的控件，返回的类型是一个列表

    :Usage:
        self.findElements(controlInfo)
    """

    def findElements(self, controlInfo):
        if controlInfo.startswith("//"):
            elements = self._driver.find_elements_by_xpath(controlInfo)
        elif ":id/" in controlInfo:
            elements = self._driver.find_elements_by_id(controlInfo)
        else:
            elements = self._driver.find_elements_by_class_name(controlInfo)
        return elements

    """
    在一个已知的控件中通过给定控件的xpatch, id 或者name来查找子控件

    :Args:
        - parentElement: 父控件，是一个已知的WebElement
        - childElementInfo: 子控件的信息，可以是xpath,id或者其他属性

    :Return:
        如果找到控件，返回第一个

    :Usage:
        self.findElement(controlInfo)
    """

    def findElementInParentElement(self, parentElement, childElementInfo):

        ele = self.findElement(parentElement)
        if childElementInfo.startswith("//"):
            element = ele.find_element_by_xpath(childElementInfo)
        elif (":id/" in childElementInfo):
            element = ele.find_element_by_id(childElementInfo)
        else:
            element = ele.find_element_by_class_name(childElementInfo)
        return element

    """
    在一个已知的控件中通过给定控件的xpatch, id 或者name来查找子控件

    :Args:
        - parentElement: 父控件，是一个已知的WebElement
        - childElementInfo: 子控件的信息，可以是xpath,id或者其他属性

    :Return:
        如果找到控件，返回所有符合条件的控件

    :Usage:
        self.findElementsInParentElement(parentElement, controlInfo)
    """

    # list 定位,返回一个列表


    def findElementsInParentElement(self, parentElement, childElementInfo):
        ele = self.findElement(parentElement)
        if childElementInfo.startswith('//'):
            elements = ele.find_elements_by_xpath(childElementInfo)
        elif ":id/" in childElementInfo or ":string/" in childElementInfo:
            elements = ele.find_elements_by_id(childElementInfo)
        else:
            elements = ele.find_elements_by_class_name(childElementInfo)
        return elements

    """
    通过UIAutomator的uia_string来查找控件

    :Args:
        -uia_string: UiSelector相关的代码，参考http://developer.android.com/
        tools/help/uiautomator/UiSelector.html#fromParent%28com.android.uiautomator.core.UiSelector%29

    :Return:
        -找到的控件

    :usage:
        self.findElementByUIAutomator(new UiSelector().(android.widget.LinearLayout))
    """

    def findElementByUIAutomator(self, uia_string):
        return self._driver.find_element_by_android_uiautomator(uia_string)

    """
    滑动操作

    :Args:
         - x1,y1,x2,y2： 滑动操作的起点和终点的坐标

    :Usage:
        self.flick(50, 50, 400, 400)
    """

    def flick(self, x1, y1, x2, y2):
        self._driver.flick(x1, y1, x2, y2)

    """
    滑动操作

    :Args:
         - x1,y1,x2,y2： 滑动操作的起点和终点的坐标
         - peroid: 多长时间内完成该操作,单位是毫秒

    :Usage:
        self.swipe(50, 50, 400, 400, 500)
    """

    def swipe(self, x1, y1, x2, y2, peroid):
        self._driver.swipe(x1, y1, x2, y2, peroid)

    def getSize(self):
        x = self._driver.get_window_size()['width']
        y = self._driver.get_window_size()['height']
        return x, y

    # 左滑 x变小,y不变
    def swipeLeft(self, t):
        s = self.getSize()
        x1 = s[0] * 0.9
        y1 = s[1] * 0.5
        x2 = s[0] * 0.1
        self.swipe(x1, y1, x2, y1, t)

    # 右滑 x变大,y不变
    def swipeRight(self, t):
        s = self.getSize()
        x1 = s[0] * 0.25
        y1 = s[1] * 0.5
        x2 = s[0] * 0.75
        self.swipe(x1, y1, x2, y1, t)

    # 上滑 x不变,y变小
    def swipeUp(self, t):
        s = self.getSize()
        x1 = s[0] * 0.5
        y1 = s[1] * 0.8
        y2 = s[0] * 0.4
        self.swipe(x1, y1, x1, y2, t)

    # 下滑 x不变,y变大
    def swipeDown(self, t):
        s = self.getSize()
        x1 = s[0] * 0.5
        y1 = s[1] * 0.25
        y2 = s[0] * 0.75
        self.swipe(x1, y1, x1, y2, t)

    def tap(self, x, y):
        self._driver.tap([(x, y)])

    """
    长按点击操作
    :Args:
     - x,y： 长按点的坐标
     - peroid: 多长时间内完成该操作,单位是毫秒

    :Usage:
        self.longPress(50, 50, 500)
    """

    def longPress(self, x, y, peroid):
        self._driver.tap([(x, y)], peroid)

    """
    点击某一个控件，如果改控件不存在则会抛出异常

    :Args:
         - elementInfo: 控件的信息，可以是xpath,id或者其他属性

    :Usage:
        self.clickElement(elementInfo)
    """
    '''
        列表定位到某个元素后,进行点击操作
    '''

    def clickListFindElements(self, parent, child, index):
        eles = self.findElementsInParentElement(parent, child)
        sleep(2)
        for i in range(len(eles)):
            if i == index:
                eles[i].click()

    def clickElement(self, elementInfo):
        element = self.findElement(elementInfo)
        element.click()

    """
    获取某个控件显示的文本，如果该控件不能找到则会抛出异常

    :Args:
         - elementInfo: 控件的信息，可以是xpath,id或者其他属性

    :Return:
        返回该控件显示的文本

    :Usage:
        self.getTextOfElement(elementInfo)

    """

    def getTextOfElement(self, elementInfo):
        element = self.findElement(elementInfo)
        return element.text

    """
    清除文本框里面的文本

    :Usage:
        self.clearTextEdit(elementInfo)
    """

    def clearTextEdit(self, elementInfo):
        element = self.findElement(elementInfo)
        element.clear()

    """
    输入框中输入文本
    """

    def sendKeys(self, elementInfo, value):
        element = self.findElement(elementInfo)
        element.send_keys(value)

    """
    隐藏键盘
    """
    def hideKeyBoard(self):
        return self._driver.hide_keyboard()

    """
    按返回键

    :Usage:
        self.pressBackKey()
    """

    def pressBackKey(self):
        # code码参考Android的官网的keycode
        self._driver.press_keycode(4)

    """
    等待某个控件显示

    :Args:
         - elementInfo: 控件的信息，可以是xpath,id或者其他属性
         - period：等待的秒数

    :Usage:
        self.waitForElement(elementInfo, 3)
    """

    def waitForElement(self, elementInfo, period):
        for i in range(0, period):
            sleep(1)
            try:
                self.findElement(elementInfo)
                return
            except:
                continue

        raise Exception("Cannot find %s in %d seconds" % (elementInfo, period))

    """
    等待某个控件不再显示

    :Args:
         - elementInfo: 控件的信息，可以是xpath,id或者其他属性
         - period：等待的秒数

    :Usage:
        self.waitForElementNotPresent(elementInfo, 3)
    """

    def waitForElementNotPresent(self, elementInfo, period):
        for i in range(0, period):
            sleep(1)
            # 不存在了则返回
            if (not self.checkElementIsShown(elementInfo)):
                return
            else:
                continue

        raise Exception("Cannot find %s in %d seconds" % (elementInfo, period))

    """
    判断某个控件是否显示

    :Args:
         - elementInfo: 控件的信息，可以是xpath,id或者其他属性
    :Return:
        True: 如果当前画面中期望的控件能被找到

    :Usage:
        self.checkElementIsShown(elementInfo)
    """

    def checkElementIsShown(self, elementInfo):
        try:
            self.findElement(elementInfo)
            return True
        except:
            return False

    """
    判断某个控件是否显示在另外一个控件中

    :Args:
        - parentElement: 父控件，是一个已知的WebElement
        - childElementInfo: 子控件的信息，可以是xpath,id或者其他属性
    :Return:
        True: 如果当前画面中期望的控件能被找到

    :Usage:
        self.checkElementShownInParentElement(elementInfo)
    """

    def checkElementShownInParentElement(self, parentElement, childElementInfo):
        try:
            self.findElementInParentElement(parentElement, childElementInfo)
            return True
        except:
            return False

    """
    判断某个控件是否被选中

    :Args:
         - elementInfo: 控件的信息，可以是xpath,id或者其他属性
    :Return:
        True: 如果当前画面中期望的控件能被选中

    :Usage:
        self.checkElementIsSelected(elementInfo)
    """

    def checkElementIsSelected(self, elementInfo):
        element = self.findElement(elementInfo)
        return element.is_selected()

    """
    判断某个开关控件是否被选中

    :Args:
         - elementInfo: 控件的信息，可以是xpath,id或者其他属性
    :Return:
        True: 如果当前画面中期望的控件能被选中

    :Usage:
        self.checkElementIsChecked(elementInfo)
    """

    def checkElementIsChecked(self, elementInfo):
        element = self.findElement(elementInfo)
        if (element.get_attribute("checked") == "false"):
            return False
        else:
            return True

    """
    判断摸个控件是否enabled
    :Args:
         - elementInfo: 控件的信息，可以是xpath,id或者其他属性
    :Return:
        True: 如果当前画面中期望的控件enabled

    :Usage:
        self.checkElementIsEnabled(elementInfo)
    """

    def checkElementIsEnabled(self, elementInfo):
        element = self.findElement(elementInfo)
        return element.get_attribute("enabled")

    """
    获取当前的Activity

    :Return:
        当前Activity的名称
    """

    def getCurrentActivity(self):
        return self._driver.current_activity

    """
    等待某一个Activity显示
    备注：不确定是否适用于ios

    :Args:
        -activityName: 某acitivity的名称
        -period: 等待的时间，秒数
    """

    def waitForActivity(self, activityName, period):
        for i in range(0, period):
            sleep(1)
            try:
                if (activityName in self.getCurrentActivity()):
                    return
            except:
                continue

        raise Exception("Cannot find the activity %s in %d seconds" % (activityName, period))

    """
    保存当前手机的屏幕截图到电脑上指定位置

    :Args:
         - pathOnPC: 电脑上保存图片的位置

    :Usage:
        self.saveScreenshot("c:\test_POI1.jpg")
    """

    def saveScreenshot(self, pathOnPC):
        self._driver.save_screenshot(pathOnPC)

    def setNetwork(self, netType):
        pass

    """
    启动测试程序
    """

    def launchApp(self):
        self._driver.launch_app()

    """
    关闭测试程序
    """

    def closeApp(self):
        self._driver.close_app()

    """
    获取测试设备的OS

    :Return: Android或者ios
    """

    def getDeviceOs(self):
        return self.desired_caps['platformName']

    """
    只打开wifi连接
    """

    def enableWifiOnly(self):
        if ((self._driver.network_connection & 0x2) == 2):
            return
        else:
            self._driver.set_network_connection(ConnectionType.WIFI_ONLY)

    """
    只打开数据连接
    """

    def enableDataOnly(self):
        if (int(self._driver.network_connection & 4) == 4):
            return
        else:
            self._driver.set_network_connection(ConnectionType.DATA_ONLY)

    """
    关闭所有网络连接
    """

    def disableAllConnection(self):
        self._driver.set_network_connection(ConnectionType.NO_CONNECTION)

    """
    获取context
    """

    def getContext(self):
        self._driver.contexts

    def switchContext(self, contextName):
        self._driver.switch_to.context(contextName)

    """
    打开所有的网络连接
    """

    def enableAllConnection(self):
        self._driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)

# 验证
# common = CommonTools()
# common.init_Driver()
