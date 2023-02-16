from typing import Optional, Any

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from pip._vendor.urllib3.connectionpool import xrange

img = cv.imread('teste1dois.JPG', 0)
ret, tresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
ret, tresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
ret, tresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
ret, tresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
ret, tresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

titles = ['Ori', 'Binary', 'Binv', 'Trunc', 'Toz', 'Tozinv']
images = [img, tresh1, tresh2, tresh3, tresh4, tresh5]

for i in xrange(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
plt.show()