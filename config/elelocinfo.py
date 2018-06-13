#!/usr/bin/python3
# -*- encoding: UTF-8 -*-

import os
import yaml

# CMD启动元素定位工具 : uiautomatorviewer
#打开yaml元素包

try:
    patth = os.getcwd()
    parent_path = os.path.dirname(patth)
    file = open(parent_path + '\\data\\elelocinfo.yaml', 'r', encoding='utf-8')
    data = yaml.load(file)
    file.close()

    # 欢迎页面元素
    first_pager = data['first_pager']['first_pager_id']
    #iframe
    frame_class = data['frame']['frame_class']
    frame_xpath = data['frame']['frame_xpath']
    #登录页面元素
    username_id = data['login']['username_id']
    password_id = data['login']['password_id']
    display_password_btn = data['login']['display_password_btn_id']
    login_btn = data['login']['login_btn_id']
    text_xy = data['login']['text_xy_id']
    #忘记密码页面元素
    #注册页面元素
    #获取权限
    inquiry_text = data['jurisdiction']['inquiry_text_id']
    number_text = data['jurisdiction']['number_text_id']
    refuse = data['jurisdiction']['refuse_id']
    allow = data['jurisdiction']['allow_id']
    #“我的”页面元素
    home_id = data['home']['home_id']
    home_xpath = data['home']['home_xpath']
    set_id = data['home']['set_id']
    home_fxpath = data['home']['home_fxpath']
    user_name_class = data['home']["user_name_class"]
    #账户设置页面元素
    logout_btn = data['account_settings']['logout_btn_id']
    #分类
    classification = data['classification']['classification_fxpath']
    #搜索
    search_bar_id = data['search']['search_bar_id']

except Exception as e:
    print('yaml文档解析失败或着元素描述错误！原因：%s' % e)