# coding:utf8
import unittest
from time import sleep
from commonTools import CommonTools


class YuxiSearchDrama(unittest.TestCase):
    def setUp(self):
        self.commontools = CommonTools()
        self.commontools.init_Driver()
        sleep(2)

    def tearDown(self):
        self.commontools.quit_Driver()

    def test_searchDrama(self):
        self.commontools.waitForElement('com.yuxip:id/iv_top_left', 2)
        self.commontools.clickElement('com.yuxip:id/iv_top_left')
        print self.commontools.getCurrentActivity()
        self.commontools.clickElement('com.yuxip:id/ll_top_search')
        # print self.commontools.getCurrentActivity()
        self.assertEqual(self.commontools.getCurrentActivity(), '.ui.activity.other.StoryListSearchActivity')
        self.commontools.waitForElement('com.yuxip:id/tv_search', 2)
        data = u'xx'
        self.commontools.sendKeys('com.yuxip:id/edit_search', data)
        self.commontools.clickElement('com.yuxip:id/tv_search')
        sleep(2)
        try:
            if self.commontools.checkElementIsShown('android.support.v7.widget.RecyclerView'):
                print u'搜索成功'
            elif self.commontools.checkElementIsShown('com.yuxip:id/tv_search_note'):
                print u'搜索没结果'
        except Exception, e:
            print e


if __name__ == '__main__':
    suite = unittest.TestCase()
    unittest.TextTestRunner(verbosity=2).run(suite)


