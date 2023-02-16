# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 17:52:44 2020

@author: cmarc
"""


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("milho2.png")

########### BLUR ###############

img2_2 = cv2.medianBlur(img, 11)

################################

img_hsv = cv2.cvtColor(img2_2, cv2.COLOR_BGR2HSV)
img_lab = cv2.cvtColor(img2_2, cv2.COLOR_BGR2LAB)

#definindo limites superiores e inferiores
lower2 = (10, 90, 10)
upper2 = (70, 255, 255)

#criando as mascaras #############
mask2 = cv2.inRange(img_hsv, lower2, upper2)
hsv = cv2.bitwise_and(img, img, mask=mask2)
img_gs = cv2.cvtColor(hsv, cv2.COLOR_BGR2GRAY)
##################################

########## TESTE ###############
#h_eq = cv2.equalizeHist(img2_2)
#img2 = cv2.Canny(img2_2, 110, 120)
################################

ret1, th1 = cv2.threshold(img_gs, 0, 255, cv2.THRESH_BINARY)
ret2, th2 = cv2.threshold(img_gs, 0, 255, cv2.THRESH_BINARY_INV)
ret3, th3 = cv2.threshold(img_gs, 0, 255, cv2.THRESH_BINARY)




res1 = cv2.bitwise_and(img, img, mask = th1 )
res2 = cv2.bitwise_and(img, img, mask = th2 )
res3 = cv2.bitwise_and(img, img, mask = th3 )

suave = np.vstack([
    np.hstack([img, res1]),
    np.hstack([res3, img2_2])
    ])


cv2.imwrite('530_7_3(1).JPG', res1)
cv2.imshow("Canny", suave)
cv2.waitKey(0)