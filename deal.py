# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 23:53:06 2020

@author: Zw
"""

import cv2
import numpy as np
#import matplotlib.pyplot as plt

#导入原图，canny检测
myimg = cv2.imread("C:/photo/1052.jpg",0)
cannyimg = cv2.Canny(myimg,20,100)

#膨胀腐蚀
kernel = np.ones((20,20),np.uint8)
kernel1 = np.ones((15,15),np.uint8)
dil_img = cv2.dilate(cannyimg,kernel,iterations = 1)

ero_img = cv2.erode(dil_img,kernel1,iterations = 1)

#输出
cv2.imwrite("C:/photo/canny.jpg",cannyimg)
cv2.imwrite("C:/photo/dil_img.jpg",dil_img)
cv2.imwrite("C:/photo/ero_img.jpg",ero_img)

#new_ca_img = cv2.Canny(dil_img,20,50)

#cv2.imwrite("C:/photo/newca.jpg",new_ca_img)

#重新读入，findcontours
n_ero_img = cv2.imread("C:/photo/ero_img.jpg")
imgray = cv2.cvtColor(n_ero_img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imgray,127,255,0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#定义边缘长度函数，排序
def length(x):
    return -cv2.arcLength(x,True)

n_contours = sorted(contours,key = length)

#创建白色图底
temp = np.ones(ero_img.shape,np.uint8)*255

#绘制最长的两条边缘
temp_img = cv2.drawContours(temp,n_contours,0,(0,255,0),3)
temp_img = cv2.drawContours(temp,n_contours,1,(0,255,0),3)

#输出
cv2.imwrite("C:/photo/temp_img.jpg",temp_img)

#边缘点数
len0 = len(n_contours[0])
len1 = len(n_contours[1])

x0 = [int(n_contours[0][i][0][0]) for i in range(len0)]
x1 = [int(n_contours[1][i][0][0]) for i in range(len1)]

"""
y0 = [int(n_contours[0][i][0][1]) for i in range(len0)]
y1 = [int(n_contours[1][i][0][1]) for i in range(len1)] 
"""

#获取坐标最大最小
xlist = sorted([max(x0),min(x0),max(x1),min(x1)])

#距离为中间两个值的差
distance = xlist[2]-xlist[1]

#绘制边界线
img_d = temp_img
for i  in range(357):
    img_d[i][303:306] = 255
    img_d[i][428:431] = 255

#图像输出
cv2.imwrite("C:/photo/img_d.jpg",img_d)
