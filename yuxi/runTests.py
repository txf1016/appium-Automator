# coding:utf8

import unittest
import resultConf
from testCases import yuxi_Chat
from testCases import yuxi_Like
from testCases import yuxi_Login

testunit = unittest.TestSuite()
testunit.addTest((unittest.makeSuite(yuxi_Chat.YuxiChat)))
testunit.addTest((unittest.makeSuite(yuxi_Like.YuxiLike)))
testunit.addTest(unittest.makeSuite(yuxi_Login.YuxiLogin))

resultConf.createReport(testunit, title=u"语戏所有用例", desc=u"语戏所有用例")
