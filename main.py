import pyautogui as gui
#import pyscreeze as eze
import cv2
import time
import os
import sys


try:
    ##x,y = gui.position()  ##得到某一点的坐标函数
    
    ##gui.moveTo(1588,700,duration = 1)
    ##gui.moveTo(196,577,duration = 1) ##移动鼠标到某位置
    ##gui.click(196,577,button = "left") ##点击一次鼠标左键
    ##gui.click(1588,700,button = "left")
    ##time.sleep(0.7)
    #第一步鼠标坐标
    X1=2648
    Y1=14

    X2=917
    Y2=44

    #第三步鼠标坐标
    X4=2308
    Y4=815
    
    #第七步鼠标坐标
    X7=2267
    Y7=910

    #第十步鼠标坐标
    X11=2601
    Y11=1561
    
    #遍历次数
    N =500

    #搜索等待时间
    T = 0.2

    #对比次数
    T1=20
    T2=10
    
    
    #第一步：初始化
    gui.click(X1,Y1,button = "left")
    time.sleep(0.2)
    gui.mouseDown()
    #time.sleep(0.2)
    gui.click(X2,Y2,button = "left")
    time.sleep(0.2)

    
############################################################
    #第二步：复制工号
    gui.hotkey('ctrl','c')
    ##time.sleep(0.3)
        
    #第四步：移动鼠标至AC搜索栏并点击两次
    gui.doubleClick(X4,Y4,button = "left")
    #time.sleep(0.1)

    #第五步：粘贴工号
    gui.hotkey('ctrl','v')
                
    #第六步：回车键
    gui.press('enter')
    #time.sleep(0.3)
#############################################################

    ##第七步：等待图片对比
    while N >0:
        #对比次数
        Num = T1
        Num2 = T2
#############################################################        
        while Num > 0:
            try:
                findPicture = gui.locateOnScreen("D:\\Desktop\\Doma.jpg",confidence=0.9)
            except:
            #等待T秒AC反应时间
                #time.sleep(T)
                Num = Num-1
                if Num == 0:
                    sys.exit()
            else:
                print('匹配成功')
                #第八步：勾选用户
                #gui.moveTo(X7,Y7,duration = 0.2)##鼠标移动到用户上边
                gui.click(X7,Y7,clicks=1,button="LEFT",duration=0.2)
                time.sleep(0.1)
                #第九步：鼠标复位
                gui.click(X2,Y2,button = "left")
                #第10步：单元格下移
                gui.press('down')
                N=N-1
                break

#############################################################
        #等待图片对比
    
        #第二步：复制工号
        time.sleep(0.2)
        gui.hotkey('ctrl','c')

        #第三步：等待AC反应时间结束，粘贴工号
        while Num2 > 0:
            try:
                findPicture = gui.locateOnScreen("D:\\Desktop\\wait.jpg",confidence=0.8)
                    
            #等待T秒AC反应时间
            except:
                time.sleep(T)
                Num2 = Num2 - 1
            else:
                #第四步：移动鼠标至AC搜索栏并点击两次
                gui.doubleClick(X4,Y4,button = "left")
                time.sleep(0.1)

                #第五步：粘贴工号
                gui.hotkey('ctrl','v')
                
                #第六步：回车键
                gui.press('enter')
                time.sleep(0.5)
                break

#############################################################           
        if Num == 0 or Num2 == 0:
            print('匹配不成功')
            #第十一步：加域提交
            gui.click(X11,Y11,button = "left")
            
            sys.exit()
            #try:
                #findPicture = gui.locateOnScreen("D:\\Desktop\\doma.jpg",confidence=0.8)
                #print (findPicture)
            #except:
                ##匹配不成功，提交加域,退出程序
                #gui.click(X10,Y10,button = "left")
                #sys.exit()
            
        
        
except KeyboardInterrupt:
    print("\n程序运行结束")


