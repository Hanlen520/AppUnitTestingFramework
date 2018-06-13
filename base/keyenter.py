
#!/usr/bin/python3
#  coding: UTF-8


import win32clipboard as w
import win32con
import win32api
def getText():#读取剪切板
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d
def setText(aString):#写入剪切板
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, aString)
    w.CloseClipboard()
if __name__=='__main__':
    a="你好"
    setText(a)#将“你好”写入剪切板
    #自动粘贴剪切板中的内容
    win32api.keybd_event(17,0,0,0)  #ctrl的键位码是17
    win32api.keybd_event(86,0,0,0)#v的键位码是86
    win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(13,0,0,0)#Enter的键位码是13
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)












