# coding:utf8
import HTMLTestRunner
import time
import pathConf


def createReport(sutie, title, desc):
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    resultname = pathConf.resultReport_path + now + "result.html"
    fp = open(resultname, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=title, description=desc)
    runner.run(sutie)
    fp.close()
