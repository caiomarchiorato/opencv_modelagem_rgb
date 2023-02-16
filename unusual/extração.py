import cv2
import numpy as np
from matplotlib import pyplot as plt

img =  cv2.imread("DSCF4385.JPG", 1)
img_gray = cv2.imread('DSCF4385.JPG', 0)
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.namedWindow('img_gray', cv2.WINDOW_NORMAL)
imgS = cv2.resize(img, (960, 540))
imgS_gray = cv2.resize(img_gray, (960, 540))

cv2.imshow('Imagem RGB', imgS)
cv2.imshow('Imagem em tons de cinza', imgS_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()



