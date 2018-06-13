#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import csv
import unittest
from basis.app_basis_driver import AppBasisDriver
from pages.app_first_page import AppFirstPage
from pages.app_login_page import AppLoginPage

# CMD启动元素定位工具 : uiautomatorviewer
# dumpsys window windows | grep -E 'mFocusedApp'
# 查看活动的包名和活动名  ：  aapt dump badging + packages
# 查看手机上应用的packageName：adb shell pm list packages
# 应用对应的apk文件在手机上的安装位置则可以在上面的命令后加-f参数:adb shell pm list packages -f
# 安装Appium客户端 ：pip install Appium-Python-Client
# Android Emulator
# 启动Appium：  appium -a 127.0.0.1 -p 4723  –U  73047c33 --no-reset   （# appium -U UDID  --app  73047c33）

# '''清理环境：
# a. 删除 “adb shell pm list package selendroid” 列出来的所有包
# b. 删除用户目录下的/AppData/Local/Temp里面的Selendroid*文件 (Appium 1.3.4以下的版本，这个文件在C盘Windows的Temp目录下)'''

#adb局域网wifi链接手机： 1、adb tcpip 5555   2、adb connect +ip   3、adb disconnect + ip

class AppTestLogin(unittest.TestCase,AppLoginPage):
    #初始化工作
    def setUp(self):
        driver = AppBasisDriver()
        self.driver = driver
        self.driver.implicitly_wait(20)
        a = AppLoginPage(self.driver)
        a.login()

    def first_page(self):
        a = AppFirstPage(self.driver)
        a.lick()


    # 退出清理工作
    def tearDown(self):
        self.driver.quit()
        pass

#
if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(NewsTest)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()
