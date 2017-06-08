# coding:utf8

import unittest
import resultConf
from testCases import init

testunit = unittest.TestSuite()
testunit.addTest(unittest.makeSuite(init.Init))

resultConf.createReport(testunit, title=u"开源中国所有用例", desc=u"开源中国所有用例")
