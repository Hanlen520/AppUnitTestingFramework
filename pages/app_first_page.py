#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from time import sleep
from basis.app_basis_page import AppBasisPage
from  config.elelocinfo import *

class AppFirstPage(AppBasisPage):

    def lick(self):
        self.driver.click(home_id)
        self.driver.click('com.yanjianjun.huozhan:id/home_tab_one')
        self.driver.click('com.yanjianjun.huozhan:id/home_tab_two')
        self.driver.click('com.yanjianjun.huozhan:id/home_tab_four')