# coding:utf8
# coding=utf8

from appium import webdriver
import unittest
import time


# import os
# PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

class test_Like(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'platformName': 'Android',
                'PlatformVersion': '5.1',
                # 'platformVersion': '5.1.1',
                # 'deviceName': '525b7d43',
                # 'deviceName': 'bf25b6c5',
                'noReset': 'true',
                'deviceName': 'YGKBBCE680444462',
                # 'app': PATH('/Users/tanxiaofen/Downloads/yx_2.5.6.apk'),
                'appPackage': 'com.yuxip',
                'appActivity': '.ui.activity.other.LoadingActivity'
            })
        time.sleep(3)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

    # def test_Like(self):
    #     # 定位到测试指定页面
    #     try:
    #         el = self.findElement('com.yuxip:id/tb_story')
    #         el.click()
    #     except Exception, e:
    #         print e
    #     time.sleep(3)
    #     try:
    #         # els = self.listFindElements('com.yuxip:id/linear_channelselect', 'com.yuxip:id/tv_item_channel_select')
    #         # type(els)
    #         # for i in range(len(els)):
    #         #     if els[i].text == u'原创':
    #         #         els[i].click()
    #         self.clickListFindElements('com.yuxip:id/linear_channelselect', 'com.yuxip:id/tv_item_channel_select',
    #                                    4)
    #     except Exception, e:
    #         print e
    #     # 返回的是一个list,代表当前页面的每个自戏的赞数控件元素
    #     eles_num = self.listFindElements('com.yuxip:id/ultimate_list', 'com.yuxip:id/tv_topic_fave_num')
    #     # 返回的是一个list,代表当前页面每个自戏的标题控件元素
    #     eles_title = self.listFindElements('com.yuxip:id/ultimate_list', 'com.yuxip:id/tv_title_hot')
    #     # 获取要点赞的剧的标题和赞数
    #     num1 = int(eles_num[1].text)
    #     title = eles_title[1].text
    #     # print num, title
    #     # 进行点击操作
    #     self.clickListFindElements('com.yuxip:id/ultimate_list', 'com.yuxip:id/tv_topic_fave_num', 1)
    #     num2 = int(eles_num[1].text)
    #     # print num1, num2, title
    #     # if num1
    #     if num2 == num1 + 1:
    #         print title + ': ' u'赞数加一'
    #     elif num2 == num1 - 1:
    #         print title + ': ' u'赞数减一'
    #     else:
    #         print title + ': ' u'点击失败'

    def test_LikeValidate(self):
        try:
            el = self.findElement('com.yuxip:id/tb_story')
            el.click()
        except Exception, e:
            print e
        time.sleep(3)
        try:
            self.clickListFindElements('com.yuxip:id/linear_channelselect', 'com.yuxip:id/tv_item_channel_select',
                                       4)
        except Exception, e:
            print e
        # eles_num = self.listFindElements('com.yuxip:id/ultimate_list', 'com.yuxip:id/tv_topic_fave_num')
        eles_title = self.listFindElements('com.yuxip:id/ultimate_list', 'com.yuxip:id/tv_title_hot')
        title = eles_title[1].text
        try:
            self.clickListFindElements('com.yuxip:id/ultimate_list', 'com.yuxip:id/tv_topic_fave_num', 1)
        except Exception, e:
            print e
        self.swipeDown(500)
        time.sleep(2)
        self.clickElement('com.yuxip:id/tb_my')
        time.sleep(2)
        self.swipeUp(1000)
        # self.clickElement('')
        time.sleep(2)
        try:
            self.clickFindElementByUIAutomator('new UiSelector().textContains("喜欢")')
        except Exception, e:
            print e
        # eles = self.listFindElement('com.yuxip:id/listview_favor_collect_activity',
        #                              'com.yuxip:id/tv_name_favor_collect_adapter')
        print title

        str1 = self.driver.page_source
        str2 = self.driver.page_source
        while str1 == str2:
            self.swipeUp(2000)
            str2 = self.driver.page_source
        else:
            print u'已滑至底部'

    # ------------------------------------------------------------方法-------------------------------------------------------------

    # 寻找元素
    def findElement(self, element):
        if element.startswith("//"):
            ele = self.driver.find_element_by_xpath(element)
        elif ":id/" in element or ":string/" in element:
            ele = self.driver.find_element_by_id(element)
        else:
            ele = self.driver.find_element_by_class_name(element)
        return ele

    def clickFindElementByUIAutomator(self, uia_string):
        return self.driver.find_element_by_android_uiautomator(uia_string).click()

    # 返回一个列表
    def listFindElements(self, parent, child):
        ele = self.findElement(parent)
        if child.startswith('//'):
            eles = ele.find_elements_by_xpath(child)
        elif ":id/" in child or ":string/" in child:
            eles = ele.find_elements_by_id(child)
        else:
            eles = ele.find_elements_by_class_name(child)
        return eles

    # 返回列表第一个
    def listFindElement(self, parent, child):
        ele = self.findElement(parent)
        if child.startswith('//'):
            eles = ele.find_element_by_xpath(child)
        elif ":id/" in child or ":string/" in child:
            eles = ele.find_element_by_id(child)
        else:
            eles = ele.find_element_by_class_name(child)
        return eles

    # list定位点击
    def clickListFindElements(self, parent, child, index):
        eles = self.listFindElements(parent, child)
        time.sleep(2)
        for i in range(len(eles)):
            if i == index:
                eles[i].click()

    # 找到元素并点击
    def clickElement(self, element):
        ele = self.findElement(element)
        ele.click()

    # 滑动
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    # 左滑 x变小,y不变
    def swipeLeft(self, t):
        s = self.getSize()
        x1 = s[0] * 0.9
        y1 = s[1] * 0.5
        x2 = s[0] * 0.1
        self.driver.swipe(x1, y1, x2, y1, t)

    # 右滑 x变大,y不变
    def swipeRight(self, t):
        s = self.getSize()
        x1 = s[0] * 0.25
        y1 = s[1] * 0.5
        x2 = s[0] * 0.75
        self.driver.swipe(x1, y1, x2, y1, t)

    # 上滑 x不变,y变小
    def swipeUp(self, t):
        s = self.getSize()
        x1 = s[0] * 0.5
        y1 = s[1] * 0.8
        y2 = s[0] * 0.4
        self.driver.swipe(x1, y1, x1, y2, t)

    # 下滑 x不变,y变大
    def swipeDown(self, t):
        s = self.getSize()
        x1 = s[0] * 0.5
        y1 = s[1] * 0.25
        y2 = s[0] * 0.75
        self.driver.swipe(x1, y1, x1, y2, t)

    # 查找元素
    def findLocal(self, element):
        x = 1
        while x == 1:
            if self.fact(element) == 1:
                self.swipeUp(2000)
                time.sleep(3)
                self.fact(element)
            else:
                print u'找到了'
                x = 2

    def fact(self, text):
        n = 1
        try:
            re = self.driver.page_source
            if text in re:
                # self.clickFindElementByUIAutomator(element)
                print u'剧点赞成功,在主页--喜欢里显示了'
        except Exception, e:
            # print u'剧取消赞成功,在主页--喜欢里没有该剧'
            return n


if __name__ == '__main__':
    suite = unittest.TestSuite()
    unittest.TextTestRunner(verbosity=2).run(suite)
