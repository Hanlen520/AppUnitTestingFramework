#!/usr/bin/env python
# coding:utf8

from base.basis_page import BasisPage


class LoginPage(BasisPage):

    LOGIN_USERNAME = "x,html/body/div[1]/div[1]/div/form/div[2]/div[2]/input[1]"
    LOGIN_PASSWAD = "x,html/body/div[1]/div[1]/div/form/div[2]/div[2]/input[2]"
    LOGIN_BUTTON = "x,html/body/div[1]/div[1]/div/form/div[2]/div[2]/button"
    ADMINISTRATOR = "x,.//*[@id='page-wrapper']/div[1]/nav/ul/li/a"
    LOGOUT_BUTTON ="x,.//*[@id='page-wrapper']/div[1]/nav/ul/li/ul/li[5]/a/div"
    IFRAME = "i,J_iframe"
    ENTER = "x,html/body/div[4]/div[7]/button[2]"
    GET_TEXT = 'x,html/body/div[1]/div'
    EXIST = "x,.//*[@id='side-menu']/li[2]/a/span"
    NOTEXIST = 'x,html/body/div[1]/div[1]/div/div/img'

    def login(self, username,password):
        driver = self.basis_driver
        self.log("输入登录用户名")
        driver.type(self.LOGIN_USERNAME,username)
        self.log("输入登录密码")
        driver.type(self.LOGIN_PASSWAD,password)
        self.log("点击登录按钮")
        driver.click(self.LOGIN_BUTTON)
        driver.sleep(3)
        

    def login_inherit(self,data):

        driver = self.basis_driver
        self.log("输入登录用户名")
        driver.type_clear(self.LOGIN_USERNAME,data['username'])
        self.log("输入登录密码")
        driver.type_clear(self.LOGIN_PASSWAD,data['password'])
        self.log("点击登录按钮")
        driver.click(self.LOGIN_BUTTON)
        driver.sleep(1)


        if data['casetype'] == 'True':
            self.log("执行登录成功用例")

            self.log("获取登陆成功的")
            self.title = driver.get_title()
            print("登陆成功的title："+self.title)

            exist = driver.isElementExist(self.EXIST)
            if exist == True:
                self.log("点击登录名")
                driver.click(self.ADMINISTRATOR)
                self.log("点击退出登录按钮")
                driver.click(self.LOGOUT_BUTTON)
                driver.sleep(3)
                self.log("点击确定按钮")
                driver.click(self.ENTER)
                driver.sleep(2)
            if exist == False:
                pass
        if data['casetype'] == 'False':
            self.log("执行登录失败用例")

            self.log("获取登录失败的断言文本")
            self.FAIL_TEXT = driver.get_text(self.GET_TEXT)
            driver.sleep(1)

            exist = driver.isElementExist(self.NOTEXIST)
            if exist == True:
                pass

            if exist == False:
                print("执行错误用例退出登陆")
                self.log("点击登录名")
                driver.click(self.ADMINISTRATOR)
                self.log("点击退出登录按钮")
                driver.click(self.LOGOUT_BUTTON)
                driver.sleep(2)
                self.log("点击确定按钮")
                driver.click(self.ENTER)
                driver.sleep(3)




