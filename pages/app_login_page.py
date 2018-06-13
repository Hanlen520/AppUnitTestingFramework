#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from time import sleep
from basis.app_basis_page import AppBasisPage
from  config.elelocinfo import *
from  config.ime import *

class AppLoginPage(AppBasisPage):


    def login(self):
        exist_first_pager = self.driver.isElementExist(first_pager)
        if exist_first_pager == True:
            self.log('开始滑动欢迎页面...')
            for i in range(4):
                self.driver.swipeLeft(600)
            self.driver.click(first_pager)
        if exist_first_pager == False:
            print("成功跳过欢迎页面")
        exist_login_btn = self.driver.isElementExist(login_btn)
        if exist_login_btn == True:
            self.log('货栈登陆中...')
            os.system(ime_appium)
            self.driver.type_clear(username_id,'15020579521')
            self.driver.type_clear(password_id,'123456')

            self.driver.click(login_btn)

        if exist_login_btn == False:
            self.log("APP已登录，开始模拟用户场景测试")

        self.log('设置允许权限')
        while True:
            exist_allow = self.driver.isElementExist(allow)
            if exist_allow == True:
                self.driver.click(allow)
            if exist_allow == False:
                self.log('权限已被设置')
                break
        sleep(2)


    def login_inherit(self, data):

        exist_first_pager = self.driver.isElementExist(first_pager)
        if exist_first_pager == True:
            self.log('开始滑动欢迎页面...')
            for i in range(4):
                self.driver.swipeLeft(600)

            self.driver.click(first_pager)

        if exist_first_pager == False:
            print("成功跳过欢迎页面")
        sleep(1)
        exist_login_btn = self.driver.isElementExist(login_btn)
        if exist_login_btn == True:
            self.log('货栈登陆中...')
            os.system(ime_appium)
            self.driver.type_clear(username_id,data['username'] )
            self.driver.type_clear(password_id, data['password'])

            self.driver.click(login_btn)

        if exist_login_btn == False:
            print("APP已登录，开始模拟用户场景测试")

        self.log('设置允许权限')
        while True:
            exist_allow = self.driver.isElementExist(allow)
            if exist_allow == True:
                self.driver.click(allow)
            if exist_allow == False:
                self.log('跳过权限设置')
                break
        if data['casetype'] == 'True':

            self.log("回家 - 获取登录成功的断言文本")
            self.driver.click(home_id)
            if self.driver.isElementExist(user_name_class) ==True :
                self.SUCCESS_TEXT = self.driver.get_text(user_name_class)
                print("断言文本："+self.SUCCESS_TEXT)
            if self.driver.isElementExist(user_name_class) == False:
                print("断言文本未能获取")
            exist_my = self.driver.isElementExist(home_id)
            if exist_my == True:
                self.log('登录成功，点击我的')
                self.driver.click(home_id)
                self.log("点击设置")
                self.driver.click(set_id)
                self.log("点击退出登录按钮")
                self.driver.click(logout_btn)
            if exist_my == False:
                self.log("登录失败，继续下一条测试用例")

        if data['casetype'] == 'False':
            try:

                self.log("获取登录失败的断言文本")
                self.FAIL_TEXT = self.driver.get_text(login_btn)
                self.log("执行登录失败用例")
                exist_login_btn = self.driver.isElementExist(login_btn)
                if exist_login_btn == True:
                    pass

                if exist_login_btn == False:
                    self.log("执行错误用例退出登陆")
                    self.log('点击我的')
                    self.driver.click(home_id)
                    self.log("点击设置")
                    self.driver.click(set_id)
                    self.log("点击退出登录按钮")
                    self.driver.click(logout_btn)
            except:
                print('未能正常运行用例'+data['number'])

