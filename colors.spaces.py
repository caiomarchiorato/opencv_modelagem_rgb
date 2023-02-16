import cv2
import numpy as np
from matplotlib import pyplot as plt

#lendo a imagem e convertendo nos espaços de cores
img = cv2.imread("milho2.png")
#hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#lab
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
#rgb
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#juntando as imagens para simplificar a visualização
numpy_horizontal_concat = np.concatenate((img, hsv), axis=1)
numpy_horizontal_concat2 = np.concatenate((lab, rgb), axis=1)
cv2.imshow('Numpy Horizontal Concat', numpy_horizontal_concat); cv2.imshow('Numpy Horizontal Concat2', numpy_horizontal_concat2)
#salvando as imagens nos espaços de cores
cv2.imwrite("Color_space1.JPEG", numpy_horizontal_concat); cv2.imwrite("Color_space2.JPEG", numpy_horizontal_concat2)


cv2.waitKey(0)
cv2.destroyAllWindows()