# coding=utf8
# coding=gb18030
from appium import webdriver
import unittest
import time


# import os
# PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class test_Mypage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'platformName': 'Android',
                'platformVersion': '5.1.1',
                'deviceName': '525b7d43',
                # 'app': PATH('/Users/tanxiaofen/Downloads/yx.apk'),
                'appPackage': 'com.yuxip',
                'appActivity': '.ui.activity.other.LoadingActivity',
                'unicodeKeyboard': True,
                'resetKeyboard': True

            })

    # 切换主页
    # def test_Change(self):
    #     print '----------------切换主页-----------------'
    #     self.getInPage()
    #     page1 = self.driver.page_source
    #     el = 'com.yuxip:id/ll_top_level'
    #     if el in page1:
    #         print '当前页面处于本体主页'
    #         # 切换至二次元主页
    #         self.driver.find_element_by_id('com.yuxip:id/iv_home_switch').click()
    #         time.sleep(5)
    #         page2 = self.driver.page_source
    #         # el2 = 'com.yuxip:id/ll_top_level'
    #         if el in page2:
    #             print '切换失败'
    #         else:
    #             print '主页切换成功,当前主页为二次元主页'
    #
    #     else:
    #         print '当前页面处于二次元主页'
    #         # 切换至本体主页
    #         self.driver.find_element_by_id('com.yuxip:id/iv_home_switch').click()
    #         time.sleep(5)
    #         page3 = self.driver.page_source
    #         if el in page3:
    #             print '主页切换成功,当前主页为本体主页'
    #         else:
    #             print '切换失败'

    # 修改用户名
    # def test_ModifyName(self):
    #     self.getInEditPage()
    #     self.modifyName()

    # # 修改用户性别
    # def test_ModifySex(self):
    #     self.getInEditPage()
    #     self.modifySex()

    # 修改用户兴趣
    def test_ModifyInterest(self):
        self.getInEditPage()
        self.modifyInterest()

    # def modifyName(self):
    #     print '----------------修改昵称-----------------'
    #     username = self.driver.find_element_by_id('com.yuxip:id/et_username')
    #     oriname = username.text
    #     print u'修改前的用户名:' + username.text
    #     username.clear()
    #     username.click()
    #     val = u'跳动的小脚丫'
    #     if val == oriname:
    #         username.send_keys(val)
    #         print u'与原名相同,不修改,返回主页'
    #         self.driver.find_element_by_id('com.yuxip:id/tv_fragment_left').click()
    #         time.sleep(2)
    #     else:
    #         username.send_keys(val)
    #         self.driver.find_element_by_id('com.yuxip:id/tv_fragment_right').click()
    #         time.sleep(3)
    #         name = self.driver.find_element_by_id('com.yuxip:id/tv_home_name').text
    #         # print type(name)
    #         if name == val:
    #             print u'用户名修改成功,当前用户名为:' + name
    #         else:
    #             print u'修改不成功'

    def modifyInterest(self):
        print '----------------修改兴趣-----------------'
        like = self.driver.find_element_by_id('com.yuxip:id/tv_info_favor')
        val = like.text
        print u'修改前的兴趣:' + val
        like.click()
        time.sleep(0.5)
        # page = self.driver.page_source
        self.driver.find_element_by_android_uiautomator('new Selector().textContains(val)').click()
        if val == u'原创':
            self.driver.find_element_by_android_uiautomator('new Selector().retextContains("同人")').click()
            self.driver.find_element_by_id('com.yuxip:id/tv_fragment_right').click()
            time.sleep(0.5)
            self.driver.find_element_by_id('com.yuxip:id/tv_fragment_right').click()
            time.sleep(1)
            re = self.driver.find_element_by_id('com.yuxip:id/tv_home_props').text
            if re == u'同人':
                print '修改成功,当前兴趣为:' + re
            else:
                print '修改失败,当前兴趣为:' + re

        else:
            self.driver.find_element_by_android_uiautomator('new Selector().textContains("原创")').click()
            self.driver.find_element_by_id('com.yuxip:id/tv_fragment_right').click()
            time.sleep(0.5)
            self.driver.find_element_by_id('com.yuxip:id/tv_fragment_right').click()
            time.sleep(1)
            re = self.driver.find_element_by_id('com.yuxip:id/tv_home_props').text
            if re == u'原创':
                print '修改成功,当前兴趣为:' + re
            else:
                print '修改失败,当前兴趣为:' + re

    # def modifySex(self):
    #     print '----------------修改性别-----------------'
    #     sexEl = self.driver.find_element_by_id('com.yuxip:id/tv_info_gender')
    #     sex = sexEl.text
    #     print u'修改前的性别是:' + sex
    #     sexEl.click()
    #     if sex == u'女':
    #         self.driver.find_element_by_id('com.yuxip:id/tv_select_camera').click()
    #         time.sleep(1)
    #         self.driver.find_element_by_id('com.yuxip:id/tv_fragment_right').click()
    #         time.sleep(2)
    #         self.driver.find_element_by_id('com.yuxip:id/iv_home_edit').click()
    #         time.sleep(1)
    #         reSex = self.driver.find_element_by_id('com.yuxip:id/tv_info_gender').text
    #         if reSex == u'男':
    #             print u'性别修改成功,当前性别为:' + reSex
    #         else:
    #             print u'性别修改不成功'
    #     else:
    #         self.driver.find_element_by_id('com.yuxip:id/tv_select_album').click()
    #         time.sleep(1)
    #         self.driver.find_element_by_id('com.yuxip:id/tv_fragment_right').click()
    #         time.sleep(2)
    #         self.driver.find_element_by_id('com.yuxip:id/iv_home_edit').click()
    #         time.sleep(1)
    #         reSex1 = self.driver.find_element_by_id('com.yuxip:id/tv_info_gender').text
    #
    #         if reSex1 == u'女':
    #             print u'性别修改成功,当前性别为:' + reSex1
    #         else:
    #             print u'性别修改不成功'

    # 获取当前页面元素
    def getPageElement(self):
        page = self.driver.page_source
        return page

    # 进入用户编辑页面
    def getInEditPage(self):
        time.sleep(5)
        self.driver.find_element_by_id('com.yuxip:id/tb_my').click()
        time.sleep(5)
        self.driver.find_element_by_id('com.yuxip:id/iv_home_edit').click()
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    unittest.TextTestRunner(verbosity=2).run(suite)
