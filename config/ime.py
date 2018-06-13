#!/usr/bin/python3
# -*- coding: UTF-8 -*-


#输入法配置
import os

ime_list='adb shell ime list -s'   #列出手机所有的输入法（dos命令）
ime_appium ='adb shell ime set io.appium.android.ime/.UnicodeIME' #appium输入法
ime_MIsougou ='adb shell ime set com.sohu.inputmethod.sogou.xiaomi/.SogouIME'  #小米搜狗输入法
ime_MIbaidu='adb shell ime set com.baidu.input_mi/.ImeService'    #小米百度输入法

#输入法调用      os.system(ime_appium)#使用appium键盘
