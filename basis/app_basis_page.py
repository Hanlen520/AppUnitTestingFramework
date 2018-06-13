#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
from basis.log import Log
from basis.app_basis_driver import AppBasisDriver


class AppBasisPage(object):
    path = os.path.abspath(os.path.dirname(os.getcwd()))
    def __init__(self,driver:AppBasisDriver):
        self.driver = driver

    def log(self,info):
        log = Log(self.path + '/logs')
        log.info(info)