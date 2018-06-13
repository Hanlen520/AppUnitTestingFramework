
from config.app_parameter import *

#参数配置
def parameter_config():
    '''
    APP和测试包的参数获取
    :return:
    '''
    __appP_bdId = AppPackage
    # __appA_udid = ".Splash"
    __appA_udid = AppActivity
    pwmode = 'lower'
    model = 'Appium'
    desired_caps = {}
    desired_caps['platformName'] = platform
    desired_caps['platformVersion'] = version
    desired_caps['noReset'] = noReset
    # self.desired_caps['unicodeKeyboard'] = unicodeK    ##未知原因，启用报错   待解决
    desired_caps['resetKeyboard'] = resetKeyboard
    desired_caps['app'] = appPath
    desired_caps['udid'] = udid
    desired_caps['deviceName'] = deviceName  # Android - ignored, iOS - iPhone name
    if platform == "Android":
        desired_caps['appPackage'] = __appP_bdId
    desired_caps['appActivity'] = __appA_udid
    if platform == "iOS":
        desired_caps['bundleId'] = __appP_bdId
        desired_caps['automationName'] = 'XCUITest'
    desired_caps['wdaLocalPort'] = localPort
    # url = "http://" + host + ":" + str(port) + "/wd/hub"
    # driver = webdriver.Remote(url, desired_caps)
    # time.sleep(3)
    # try:
    #     self.driver = driver
    #
    # except Exception:
    #     raise NameError("APP %s Not Found!" % platform)
    return desired_caps


# CMD启动元素定位工具 : uiautomatorviewer
# dumpsys window windows | grep -E 'mFocusedApp'
# 查看活动的包名和活动名  ：  aapt dump badging + packages（可以是包的路径，很重要）
# 查看手机上应用的packageName：adb shell pm list packages
# 应用对应的apk文件在手机上的安装位置则可以在上面的命令后加-f参数:adb shell pm list packages -f
# 安装Appium客户端 ：pip install Appium-Python-Client
# Android Emulator
# 启动Appium：  appium -a 127.0.0.1 -p 4723  –U  73047c33 --no-reset   （# appium -U UDID  --app  73047c33）
#
# '''清理环境：
# a. 删除 “adb shell pm list package selendroid” 列出来的所有包
# b. 删除用户目录下的/AppData/Local/Temp里面的Selendroid*文件 (Appium 1.3.4以下的版本，这个文件在C盘Windows的Temp目录下)'''
#
# adb局域网wifi链接手机： 1、adb tcpip 5555   2、adb connect +ip   3、adb disconnect + ip
#
#
# cmd命令中输入：adb shell 进入shell命令模式
# shell中输入：logcat | grep ActivityManager
#
# 查看包名和活动名  cmd命令中输入：adb shell dumpsys activity activities
#
# dos查看端口    netstat -ano|findstr '4723'