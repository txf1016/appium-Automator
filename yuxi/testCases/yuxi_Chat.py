# coding=utf8
import unittest
import time
from commonTools import CommonTools


class yuxiChat(unittest.TestCase):
    def setUp(self):
        self.commontools = CommonTools()
        self.commontools.init_Driver()
        time.sleep(3)

    def tearDown(self):
        self.commontools.quit_Driver()

    def testChat(self):
        self.getPage()
        self.commontools.clickElement('com.yuxip:id/et_yx_text')
        time.sleep(2)
        for i in range(100):
            self.commontools.sendKeys('com.yuxip:id/et_yx_text', u'戏文')
            self.commontools.clickElement('com.yuxip:id/tv_text_send')
            time.sleep(0.5)

    def getPage(self):
        self.commontools.clickElement('com.yuxip:id/tb_chat')
        time.sleep(2)
        # 列表定位
        self.commontools.clickListFindElements('com.yuxip:id/listView', 'com.yuxip:id/shop_name', u'星辰')
        time.sleep(3)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    unittest.TextTestRunner(verbosity=2).run(suite)
