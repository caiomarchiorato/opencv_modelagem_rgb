# importando os pacotes necessarios
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

# carrega e mostra a imagem
image = cv2.imread("milho.jpg")
image2 = cv2.imread("milho.jpg")
cv2.imshow("image", image)

#convertendo a imagem para escala de cinza e criando o histogram
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

plt.figure()
plt.title("Histogram em escala de cinza")
plt.xlabel("Bins")
plt.ylabel("Número de pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()