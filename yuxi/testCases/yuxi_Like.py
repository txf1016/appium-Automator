# coding=utf8

import unittest
import time
from commonTools import CommonTools


class YuxiLike(unittest.TestCase):
    def setUp(self):
        self.commontools = CommonTools()
        self.commontools.init_Driver()
        time.sleep(3)

    def tearDown(self):
        self.commontools.quit_Driver()

    def test_Like(self):
        # 定位到测试指定页面
        try:
            self.commontools.clickElement('com.yuxip:id/tb_story')
        except Exception, e:
            print e
        # time.sleep(2)
        self.commontools.waitForElement('com.yuxip:id/linear_channelselect', 2)
        try:
            self.commontools.clickListFindElements('com.yuxip:id/linear_channelselect',
                                                   'com.yuxip:id/tv_item_channel_select', 4)
        except Exception, e:
            print e
        # 刷新页面
        time.sleep(2)
        self.commontools.swipeDown(1000)

        # 对记录进行点赞或取消赞

        self.commontools.findElement('com.yuxip:id/ultimate_list')
        # 返回的是一个list,代表当前页面的每个自戏的赞数控件元素
        eles_num = self.commontools.findElementsInParentElement('com.yuxip:id/ultimate_list',
                                                                'com.yuxip:id/tv_topic_fave_num')

        # 返回的是一个list,代表当前页面每个自戏的标题控件元素
        eles_title = self.commontools.findElementsInParentElement('com.yuxip:id/ultimate_list',
                                                                  'com.yuxip:id/tv_title_hot')
        # 获取要点赞的剧的标题和赞数
        num1 = int(eles_num[1].text)
        title = eles_title[1].text
        # 进行点击操作
        self.commontools.clickListFindElements('com.yuxip:id/ultimate_list', 'com.yuxip:id/tv_topic_fave_num', 1)
        num2 = int(eles_num[1].text)
        if num2 == num1 + 1:
            print title + ': ' u'赞数加一'
        elif num2 == num1 - 1:
            print title + ': ' u'赞数减一'
        else:
            print title + ': ' u'点击失败'


# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     unittest.TextTestRunner(verbosity=2).run(suite)
