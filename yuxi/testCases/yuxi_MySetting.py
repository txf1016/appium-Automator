# coding=utf8

from appium import webdriver
import unittest
import time


import os
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

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
                # 'deviceName': 'YGKBBCE680444462',
                'app': PATH('/Users/tanxiaofen/Downloads/yx_2.5.6.apk'),
                'appPackage': 'com.yuxip',
                'appActivity': '.ui.activity.other.LoadingActivity'
            })

    def getInPage(self):
        time.sleep(2)
        self.driver.find_element_by_id('com.yuxip:id/tb_my').click()
        time.sleep(0.5)
        self.driver.find_element_by_id('com.yuxip:id/iv_home_setting').click()
        time.sleep(0.5)

    def test_feedBack(self):
        self.driver.find_element_by_id('com.yuxip:id/feedback').click()
        
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    unittest.TextTestRunner(verbosity=2).run(suite)
