# coding=utf8

from appium import webdriver
import unittest
import time
import os

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class test_Install(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'platformName': 'Android',
                'platformVersion': '5.1.1',
                'deviceName': '34ebfa7d',
                'app': PATH('/Users/tanxiaofen/Downloads/yx.apk'),
                'appPackage': 'com.yuxip',
                'appActivity': '.ui.activity.other.LoadingActivity'
            })

    def test_installed(self):
        yx = self.driver.is_app_installed('com.yuxip')
        if yx:
            # print u'当前的Activity是' + self.driver.current_activity
            time.sleep(5)
            print u'---跳过欢迎页---'
            self.driver.find_element_by_id('com.yuxip:id/loading_skip').click()
            time.sleep(1)
            # self.assertEqual(self.driver.current_activity, '.ui.activity.other.LoginMobileActivity', u'跳过失败')

            if self.driver.current_activity == '.ui.activity.other.LoginMobileActivity':
                print u'跳过,进入登录页面成功'
            else:
                print u'跳过失败'
            time.sleep(1)
        else:
            self.driver.install_app('/Users/tanxiaofen/Downloads/yx.apk')
            time.sleep(10)

    def test_welcome(self):
        print u'---欢迎页---'
        for i in range(5):
            print u'启动页滑动开始执行', i
            self.driver.swipe(600, 600, 200, 600, 500)
            time.sleep(2)
        time.sleep(2)
        self.driver.find_element_by_id('com.yuxip:id/loading_start').click()
        if self.driver.current_activity == '.ui.activity.other.LoginMobileActivity':
            print u'点击【进入新世界】,进入登录页面成功'
        else:
            print u'进入新世界失败'
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    unittest.TextTestRunner(verbosity=2).run(suite)
