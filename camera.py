# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 22:25:11 2020

@author: Zw
"""

import cv2

#拍照函数
def takephoto():
#摄像头初始化
    cap = cv2.VideoCapture(0)

#设置图像尺寸
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,500)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,500)

    retval , img =cap.read()

#保存原图片
    cv2.imwrite("newimg",img)  #注意路径
    
    None = cv2.VideoCapture.release()

