#!/usr/bin/env python
# coding:utf8
import csv
import unittest
from base.basis_driver import BasisDriver, BasisBrowser
from pages.login_page import LoginPage

'''在本文件运行时路径需要加../ 
    在unittest框架运行时不需要加../'''
class WebTestLogin(unittest.TestCase,LoginPage):

    Adress = '192.168.1.195'
    BASIS_BROWSER = BasisBrowser.Chrome


    '''使用basis_driver'''
    def setUp(self):
        # self.URL = "http://" + self.Adress + ":8081/bi"
        self.URL = "http://192.168.1.195:8081/bi"
        self.driver = BasisDriver(self.BASIS_BROWSER)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = self.URL
        self.LOGINPAGE = LoginPage(self.driver,self.base_url)   #实例化LoginPage作为局部变量时使用
        self.LOGINPAGE.open("")

    def tearDown(self):
        self.driver.quit_browser()
        # self.csv_file.close()


    '''使用csv文件传参'''
    def test_csv_login(self):

        self.log("打开csv文件")
        '''csv文件路径(path)使用main.py运行时,相对路径无需加( ../ )。
          使用test调试时必须加( ../ ),大多数情况必须使用绝对路径'''
        # #main.py运行
        # self.csv_file = open(r'data/case.xlsx',  #csv文件路径
        #                 mode = 'r',     #获得文件权限
        #                 encoding = 'utf8')  #字符集
        #test调试
        self.csv_file = open(r'../data/case.xlsx',  # csv文件路径
                             mode='r',  # 获得文件权限
                             encoding='utf8')  # 字符集

        self.log("读取csv文件")
        csv_data = csv.reader(self.csv_file)

        self.log("跳过第一行数据")
        is_header = True
        for line in csv_data:
            if is_header:
                is_header = False
                continue    #跳出本次循环

            self.log('csv文件数据生成字典')
            data = {'number':line[0],
                    'username':line[1],
                    'password':line[2],
                    'casetype':line[3]}

            self.log("实例化LoginPage作为局部变量")
            LOGINPAGE = LoginPage(self.driver,self.base_url)
            self.log("调用对象LoginPage中的方法login_inherit并传递(data dict)参数")
            LOGINPAGE.login_inherit(data)

            self.log("开始执行断言")
            if data['casetype'] == 'True':
                self.log("获取断言文本1")
                TITLE = LOGINPAGE.title
                '''调用断言方法“截图”和“断言日志”文件路径(path)使用main.py运行时,
                相对路径无需加( ../ )。使用test调试时必须加( ../ ),必要时使用绝对路径'''
                # # main.py运行
                # self.driver.assertion_log(TITLE,
                #                           "睿思BI - 数据可视化分析系统",
                #                           "\nTrue断言失败:" + data['number']+
                #                           "\n断言生成时间："+
                #                           (time.strftime("%Y/%m/%d-%H:%M:%S",time.localtime()))+"\n",
                #                           'screenshots',
                #                           r'logs_assert/assert_true.txt')
                # test调试
                self.driver.assertion_log(TITLE,
                                          "睿思BI - 数据可视化分析系统",
                                          "True断言失败:" + data['number'],
                                          r'../screenshots',
                                          r'../logs_assert/assert_true.txt')

            if data['casetype'] == 'False':
                self.log("获取断言文本2")
                text = LOGINPAGE.FAIL_TEXT
                self.log("执行登录失败断言")
                '''调用断言方法“截图”和“断言日志”文件路径(path)使用main.py运行时,
                相对路径无需加( ../ )。使用test调试时必须加( ../ ),必要时使用绝对路径'''
                # # main.py运行
                # self.driver.assertion_log(text,
                #                           " 账号不存在，请确认账号是否输入正确！ ",
                #                           "\nFalse断言失败:" +
                #                           data['number']+"\n断言生成时间："+
                #                           (time.strftime("%Y/%m/%d-%H:%M:%S",time.localtime()))+"\n",
                #                           'screenshots',
                #                           r'logs_assert/assert_false.txt')
                # test调试
                self.driver.assertion_log(text,
                                          " 账号不存在，请确认账号是否输入正确！ ",
                                          "False断言失败:" + data['number'],
                                          r'../screenshots',
                                          r'../logs_assert/assert_false.txt')

        # self.log("关闭csv文件")
        # csv_file.close()
    '''使用数据库数据传参'''
    # def test_sql_login(self):
    #
    #     sql_data = self.driver.get_sql_data(
    #         r'..\WEB_TEST\data\login_mysql.sql',    #xx.sql文件路径(file_path)
    #         'r',        #xx.sql文件读取权限(file_reservation)
    #         'utf8',     #xx.sql文件字符集（character_set）
    #         self.Adress,    # 数据库所在机器的地址（adress）
    #         'root',         #数据库用户名(username)
    #         None,           #数据库密码（password为空时可写：None）
    #         'rs_report',    # 数据库(database)
    #         3306,            # 端口（port不要加引号）
    #         'utf8')         # 数据库字符集（charset防止读取数据库数据出现乱码）
    #     try:
    #         for line in sql_data:
    #             data = {'username': line[0],
    #                     'password':123456,
    #                     'casetype':line[2]}
    #             # self.log("实例化LoginPage作为局部变量")
    #             LOGINPAGE = LoginPage(self.driver,self.base_url)
    #             # self.log("调用对象LoginPage中的方法login_inherit并传递(data dict)参数")
    #             LOGINPAGE.login_inherit(data)
    #
    #             # self.log("开始执行断言")
    #             if data['casetype'] == 'True':
    #                 self.log("获取断言文本")
    #                 text = LOGINPAGE.TURE_TEXT
    #                 self.log("执行登录成功断言")
    #                 self.assertEqual('睿思BI - 系统介绍',text,'登录失败')
    #             if data['casetype'] == 'False':
    #                 self.log("获取断言文本")
    #                 text = LOGINPAGE.FAIL_TEXT
    #                 self.log("执行登录失败断言")
    #                 self.assertEqual('账号不存在，请确认账号是否输入正确！',text,'断言失败')
    #     except:
    #         # self.log("抓取断言失败屏幕截图")
    #         self.driver.get_screenshot('screenshots')
    #     finally:
    #         # self.log("关闭数据库")
    #         self.driver.close_sql()

if __name__ == '__main__':
    unittest.main()
