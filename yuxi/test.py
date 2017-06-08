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

    def test_Like(self):
        # 定位到测试指定页面
        time.sleep(5)
        try:
            el = self.findElement('com.yuxip:id/tb_story')
            el.click()
        except Exception, e:
            print e
        time.sleep(3)
        try:
            # els = self.listFindElements('com.yuxip:id/linear_channelselect', 'com.yuxip:id/tv_item_channel_select')
            # type(els)
            # for i in range(len(els)):
            #     if els[i].text == u'原创':
            #         els[i].click()
            self.clickListFindElements('com.yuxip:id/linear_channelselect', 'com.yuxip:id/tv_item_channel_select',
                                       u'原创')

        except Exception, e:
            print e

    # 寻找元素
    def findElement(self, element):
        if element.startswith("//"):
            ele = self.driver.find_element_by_xpath(element)
        elif ":id/" in element or ":string/" in element:
            ele = self.driver.find_element_by_id(element)
        else:
            ele = self.driver.find_element_by_class_name(element)
        return ele

    def listFindElements(self, parent, child):
        ele = self.findElement(parent)
        if child.startswith('//'):
            eles = ele.find_elements_by_xpath(child)
        elif ":id/" in child or ":string/" in child:
            eles = ele.find_elements_by_id(child)
        else:
            eles = ele.find_elements_by_class_name(child)
        return eles

    def clickListFindElements(self, parent, child, value):
        eles = self.listFindElements(parent, child)
        time.sleep(2)
        for i in range(len(eles)):
            if eles[i].text == value:
                eles[i].click()

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    unittest.TextTestRunner(verbosity=2).run(suite)
