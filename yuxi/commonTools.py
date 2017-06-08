# coding:utf8

from appium import webdriver
import pathConf
from desConf import DesConf


class CommonTools:
    remoteHost = 'http://127.0.0.1:4723/wd/hub'

    def __init__(self):
        self._driver = None
        self.androidDes = DesConf().android_Des
        self.androidDes['app'] = pathConf.app_name_path

    def init_Driver(self):
        # DesConf.android_Des['app'] = pathConf.app_name_path
        #  # 'app': PATH('//Users/tanxiaofen/Downloads/inface.zip') IOS
        # print DesConf.android_Des
        self._driver = webdriver.Remote(self.remoteHost, self.androidDes)

    def quit_Driver(self):
        if (self._driver):
            self._driver.quit()


# 验证
# common = CommonTools()
# common.init_Driver()
