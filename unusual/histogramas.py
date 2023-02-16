#importando os pacotes
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("milho.png")
img_GS = cv2.imread("milho.png", 0)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
#cv2.imshow("img", img_GrayScale);
plt.show()


h_eq = cv2.equalizeHist(img_GS)
plt.figure()
plt.title("Histograma equalizado")
plt.xlabel("Intensidade")
plt.ylabel("Qt de pixels")
plt.hist (h_eq.ravel(), 256, [0,256])
plt.xlim([0,256])
plt.ylim([0, 8000])
plt.show()

cv2.imshow("Normal", img)
cv2.imshow("Eq", h_eq)

cv2.waitKey()

#lendo a imagem
img = cv2.imread("milho.png")
#criando um vetor de espectros
color = ('b', 'g', 'r')
#usando os espectros em um loop para concatenar os gráficos dos espectros
for i,col in enumerate(color):
    hist = cv2.calcHist([img],[i],None , [256], [0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])
    plt.ylim([0, 6000])
plt.show()
#Separa os canais

