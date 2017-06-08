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
                'PlatformVersion': '4.4.4',
                # 'platformVersion': '5.1.1',
                # 'deviceName': '525b7d43',
                'deviceName': 'bf25b6c5',
                'noReset': 'true',
                # 'deviceName': 'YGKBBCE680444462',
                # 'app': PATH('/Users/tanxiaofen/Downloads/yx_2.5.6.apk'),
                'appPackage': 'com.yuxip',
                'appActivity': '.ui.activity.other.LoadingActivity'
            })

    # 获取页面大小
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    # 向下刷新页面
    def swipeDown(self, t):
        l = self.getSize()
        x1 = 0.5 * l[0]
        y1 = 0.25 * l[1]
        y2 = 0.75 * l[1]
        self.driver.swipe(x1, y1, x1, y2, t)

    def swipeUp(self, t):
        l = self.getSize()
        x1 = 0.5 * l[0]
        y1 = 0.25 * l[1]
        y2 = 0.75 * l[1]
        self.driver.swipe(x1, y2, x1, y1, t)

    def test_Like(self):
        # 定位到测试指定页面
        time.sleep(5)
        try:
            self.driver.find_element_by_id('com.yuxip:id/tb_story').click()
        except Exception, e:
            print e
        time.sleep(2)
        item = self.driver.find_element_by_id('com.yuxip:id/linear_channelselect')
        items = item.find_elements_by_id('com.yuxip:id/tv_item_channel_select')
        items[4].click()
        time.sleep(5)
        self.swipeDown(1000)

        # 对第一条记录点赞或取消点赞
        element = self.driver.find_element_by_id('com.yuxip:id/ultimate_list')
        # element = self.listFindElements('com.yuxip:id/ultimate_list','com.yuxip:id/iv_topic_fave')
        elements = element.find_elements_by_id('com.yuxip:id/iv_topic_fave')

        # 第一条记录初始的赞数
        num = element.find_elements_by_id('com.yuxip:id/tv_topic_fave_num')
        i = int(num[0].text)

        # 获取剧的title
        title = element.find_elements_by_id('com.yuxip:id/tv_title_hot')
        re = title[0].text

        # 点赞
        elements[0].click()
        time.sleep(3)
        self.swipeDown(500)

        # 第一条记录操作后的赞数
        num1 = element.find_elements_by_id('com.yuxip:id/tv_topic_fave_num')
        j = int(num1[0].text)

        if j == i - 1:
            print re + u':该剧你点过赞,赞数减1'
            self.likePage()
            page = self.driver.page_source
            if re in page:
                print u'取消赞不成功,页面仍显示:' + re
            else:
                print u'取消赞成功,页面不显示:' + re
        elif j == i + 1:
            print re + u':该剧你没有点过赞,赞数加1'
            self.likePage()
            page = self.driver.page_source
            if re in page:
                print u'点赞成功,页面显示:' + re
            else:
                print u'点赞不成功,页面没显示:' + re

        else:
            print u'点赞/取消赞出错'

    # 查看喜欢页面

    def likePage(self):
        self.driver.find_element_by_id('com.yuxip:id/tb_my').click()
        time.sleep(5)
        self.swipeUp(500)
        try:
            self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("喜欢")').click()
        except Exception, e:
            print e
        time.sleep(3)

    # 寻找元素
    def findElement(self, element):
        if element.startswitch('//'):
            self.ele = self.driver.find_element_by_xpath(element)
        elif 'id:/' in element or 'string:/' in element:
            self.ele = self.driver.find_element_by_id(element)
        else:
            self.ele = self.driver.find_element_by_class_name(element)
        return self.ele

    # List定位
    def listFindElements(self, parent, child):
        el1 = self.findElement(parent)
        if child.startswith('//'):
            el2 = el1.find_element_by_xpath(child)
        elif 'id:/' in child or 'string:/' in child:
            el2 = el1.find_element_by_id(child)
        else:
            el2 = el1.find_element_by_class_name(child)
        return el2

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    unittest.TextTestRunner(verbosity=2).run(suite)
