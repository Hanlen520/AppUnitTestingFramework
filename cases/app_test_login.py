#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import csv,ddt,time,unittest
from pages.app_login_page import AppLoginPage
from  config.ime import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
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
from basis.app_basis_driver import AppBasisDriver
class AppTestLogin(unittest.TestCase,AppLoginPage):
    #初始化工作
    def setUp(self):
        driver = AppBasisDriver()
        self.driver = driver
        self.driver.implicitly_wait(20)

    @ddt.ddt
    def test_login_inherit(self):

        self.driver.xlsx_csv("/data/case.xlsx",'login', "/data/csv/login.csv")
        self.log("打开csv文件")
        csv_file = open(self.path + '/data/csv/login.csv',  # csv文件路径
                             mode='r',  # 获得文件权限
                             encoding='utf8')  # 字符集

        self.log("读取csv文件")
        csv_data = csv.reader(csv_file)

        self.log("跳过第一行数据")
        is_header = True
        for line in csv_data:
            if is_header:
                is_header = False
                continue

            self.log('csv文件数据生成字典')
            data = {'number': line[0],
                    'username': line[1],
                    'password': line[2],
                    'casetype': line[3]}

            testlogin = AppLoginPage(self.driver)
            testlogin.login_inherit(data)
            try:
                self.log("开始执行断言")

                if data['casetype'] == 'True':

                    self.log("获取page断言文本 - 成功")
                    TITLE = testlogin.SUCCESS_TEXT
                    self.log("执行登录成功断言")
                    self.driver.assertion_log(TITLE,
                                              "15020579521",
                                              "\nTrue断言失败:" + data['number']+
                                              "\n断言生成时间："+
                                              (time.strftime("%Y/%m/%d-%H:%M:%S",time.localtime()))+"\n",
                                              r'/screenshots',
                                              r'/logs_assert/assert_true.txt')



                if data['casetype'] == 'False' or data['casetype'] == '':
                    self.log("获取page断言文本 - 失败")
                    text = testlogin.FAIL_TEXT
                    self.log("执行登录失败断言")
                    self.driver.assertion_log(text,
                                              "登录",
                                              "\nFalse断言失败:" +
                                              data['number']+"\n断言生成时间："+
                                              (time.strftime("%Y/%m/%d-%H:%M:%S",time.localtime()))+"\n",
                                              r'/screenshots',
                                              r'/logs_assert/assert_false.txt')
            except:
                print('未能正常运行用例' + data['number'])

        self.log("关闭csv文件")
        csv_file.close()

    #退出清理工作
    def tearDown(self):
        self.driver.quit()
        os.system(ime_MIsougou)
        pass


if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(NewsTest)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()
