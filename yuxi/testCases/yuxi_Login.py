# coding=utf8
from appium import webdriver
import unittest
from time import sleep


# import os


# PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class test_Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'platformName': 'Android',
                # 'platformVersion': '5.1.1',
                'PlatformVersion': '4.4.4',
                # oppo
                # 'deviceName': '34ebfa7d',
                # 红米1s
                'deviceName': 'bf25b6c5',
                # 'app': PATH('/Users/tanxiaofen/Downloads/yx.apk'),
                'appPackage': 'com.yuxip',
                'appActivity': '.ui.activity.other.LoadingActivity',
                'unicodeKeyboard': True,
                'resetKeyboard': True
            })

    def quitLogin(self):
        print u'-------判断是否已登录-------'
        sleep(2)
        if self.driver.current_activity == '.ui.activity.other.MainActivity':
            print u'用户已登录,需退出'
            self.driver.find_element_by_id('com.yuxip:id/tb_my').click()
            sleep(5)
            self.driver.find_element_by_id('com.yuxip:id/iv_home_setting').click()
            sleep(2)
            self.driver.find_element_by_id('com.yuxip:id/exit').click()
            sleep(2)
            self.driver.find_element_by_id('com.yuxip:id/tv_confirm').click()
            sleep(2)
            if self.driver.current_activity == '.ui.activity.other.LoginMobileActivity':
                print u'退出成功'
            else:
                print u'退出失败'
            sleep(2)
        else:
            print u'用户处于退出状态,请登录'

    def test_Mobile(self):
        self.quitLogin()
        print u'-----手机号登录-----'
        sleep(5)
        self.driver.find_element_by_id('com.yuxip:id/iv_login_mobile').click()
        sleep(1)
        # print self.driver.current_activity
        mb = self.driver.find_element_by_id('com.yuxip:id/et_login_name')
        pw = self.driver.find_element_by_id('com.yuxip:id/et_login_password')
        btn = self.driver.find_element_by_id('com.yuxip:id/tv_login_btn')
        mb.click()
        sleep(1)
        mb.send_keys('18910599092')
        pw.click()
        pw.send_keys('123456')
        self.driver.hide_keyboard()
        sleep(2)
        btn.click()
        # self.driver.wait_activity('.ui.activity.other.MainActivity', 5, 1)
        sleep(10)
        if self.driver.current_activity == '.ui.activity.other.MainActivity':
            print u'手机号登录成功'
        else:
            print u'手机号登录失败'

    # def test_weiBo(self):
    #     self.quitLogin()
    #     print u'-----微博登录-----'
    #     sleep(5)
    #     self.driver.find_element_by_id('com.yuxip:id/iv_login_sina').click()
    #     sleep(10)
    #     if self.driver.current_activity == '.ui.activity.other.MainActivity':
    #         print u'微博登录成功'
    #     else:
    #         print u'微博登录失败'

    def test_qQ(self):
        self.quitLogin()
        print u'-----QQ登录-----'
        sleep(8)
        self.driver.find_element_by_id('com.yuxip:id/iv_login_qq').click()
        sleep(3)
        self.driver.find_element_by_class_name('android.widget.Button').click()
        sleep(5)
        if self.driver.current_activity == '.ui.activity.other.MainActivity':
            print u'QQ登录成功'
        else:
            print u'QQ登录失败'

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    unittest.TextTestRunner(verbosity=2).run(suite)
