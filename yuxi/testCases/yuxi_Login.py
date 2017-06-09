# coding=utf8
# from appium import webdriver
import unittest
from time import sleep
from commonTools import CommonTools


class YuxiLogin(unittest.TestCase):
    def setUp(self):
        self.commontools = CommonTools()
        self.commontools.init_Driver()
        sleep(2)

    def tearDown(self):
        self.commontools.quit_Driver()

    def test_yuxiMbLogin(self):
        # print self.commontools.getCurrentActivity()
        if self.commontools.getCurrentActivity() == '.ui.activity.other.LoginMobileActivity':
            print u'处于登出状态: 进行登录操作'
            self.yuxi_MbLoginIn()
        else:
            print u'处于登录状态: 进行登出再登录操作'
            self.yuxi_LoginOut()
            self.yuxi_MbLoginIn()

    # 语戏手机登录
    def yuxi_MbLoginIn(self):
        self.commontools.waitForElement('com.yuxip:id/iv_login_mobile', 2)
        self.commontools.clickElement('com.yuxip:id/iv_login_mobile')
        self.commontools.sendKeys('com.yuxip:id/et_login_name', '10000000008')
        sleep(2)
        self.commontools.sendKeys('com.yuxip:id/et_login_password', '123')
        # self.commontools.hideKeyBoard()
        self.commontools.clickElement('com.yuxip:id/tv_login_btn')
        sleep(2)
        try:
            if self.commontools.getCurrentActivity() != '.ui.activity.other.LoginMobileActivity':
                print u'登录成功'
        except Exception, e:
            print e

    # 语戏退出登录
    def yuxi_LoginOut(self):
        self.commontools.waitForElement('com.yuxip:id/tb_my', 5)
        self.commontools.clickElement('com.yuxip:id/tb_my')
        self.commontools.waitForElement('com.yuxip:id/iv_home_setting', 2)
        self.commontools.clickElement('com.yuxip:id/iv_home_setting')
        self.assertEqual(self.commontools.getCurrentActivity(), '.ui.activity.home.MySettingActivity')
        # print self.commontools.getCurrentActivity()
        self.commontools.clickElement('com.yuxip:id/exit')
        self.commontools.waitForElement('com.yuxip:id/tv_confirm', 1)
        self.commontools.clickElement('com.yuxip:id/tv_confirm')
        self.assertEqual(self.commontools.getCurrentActivity(), '.ui.activity.other.LoginMobileActivity')

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

        # def test_qQ(self):
        #     self.quitLogin()
        #     print u'-----QQ登录-----'
        #     sleep(8)
        #     self.driver.find_element_by_id('com.yuxip:id/iv_login_qq').click()
        #     sleep(3)
        #     self.driver.find_element_by_class_name('android.widget.Button').click()
        #     sleep(5)
        #     if self.driver.current_activity == '.ui.activity.other.MainActivity':
        #         print u'QQ登录成功'
        #     else:
        #         print u'QQ登录失败'


# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     unittest.TextTestRunner(verbosity=2).run(suite)
