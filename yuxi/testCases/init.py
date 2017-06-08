# coding:utf8
import unittest
from time import sleep
from commonTools import CommonTools


class Init(unittest.TestCase):
    def setUp(self):
        self.commonTools = CommonTools()
        self.commonTools.init_Driver()

    def tearDown(self):

        self.commonTools.quit_Driver()

    def test_yuxiInit(self):
        sleep(3)

#
# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     unittest.TextTestRunner(verbosity=2).run(suite)
