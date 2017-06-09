# coding=utf8
# coding=gb18030
from appium import webdriver
import unittest
import time


# import os
# PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class test_Chat(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'platformName': 'Android',
                'platformVersion': '5.1',
                # 'deviceName': '525b7d43',
                'deviceName': 'YGKBBCE680444462',
                # 'app': PATH('/Users/tanxiaofen/Downloads/yx.apk'),
                'appPackage': 'com.yuxip',
                'appActivity': '.ui.activity.other.LoadingActivity',
                'unicodeKeyboard': True,
                'resetKeyboard': True

            })

    def testChat(self):
        self.getPage()
        text = self.driver.find_element_by_id('com.yuxip:id/et_yx_text')
        text.click()
        time.sleep(1)
        for i in range(100):
            text.send_keys('t')
            self.driver.find_element_by_id('com.yuxip:id/tv_text_send').click()
            time.sleep(0.5)

    def getPage(self):
        time.sleep(3)
        self.driver.find_element_by_id('com.yuxip:id/tb_chat').click()
        time.sleep(1)
        el = self.driver.find_element_by_id('com.yuxip:id/listView')
        els = el.find_elements_by_class_name('android.widget.RelativeLayout')
        els[0].click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    unittest.TextTestRunner(verbosity=2).run(suite)
