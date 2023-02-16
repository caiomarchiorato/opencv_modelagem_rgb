# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 11:23:14 2020

@author: cmarc
"""


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("milho5.png")
img_gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

########## TESTE ###############

#h_eq = cv2.equalizeHist(img_gs)

#img2_2 = cv2.medianBlur(img_gs, 7)
#img2 = cv2.Canny(img2_2, 110, 120)

#canny = cv2.bitwise_and(img, img, mask = img2 )
#cv2.imshow("Canny", canny)
#cv2.waitKey(0)

#################################


###### suavização da máscara ########
blur = cv2.GaussianBlur(img_gs,(9,9),0)
blur2 = cv2.medianBlur(img_gs,11)

###### aplicação de limiar ########
ret, th1 = cv2.threshold(img_gs, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
ret2, th2 = cv2.threshold(img_gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
ret4, th4 = cv2.threshold(blur2, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

###### aplicando máscara ##########

res = cv2.bitwise_and(img, img, mask = th1)
res2 = cv2.bitwise_and(img, img, mask = th2)
res3 = cv2.bitwise_and(img, img, mask = th3)
res4 = cv2.bitwise_or(img, img, mask = th4)

##### Organizando o plot
suave = np.vstack([
    np.hstack([res, res2]),
    np.hstack([res3, res4])
    ])

##### plotando as imagens
cv2.imshow("img", suave)
cv2.waitKey(0)
