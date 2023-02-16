#importando os pacotes
import cv2
import numpy as np
from matplotlib import pyplot as plt

#lendo a imagem
img = cv2.imread("milho2.png")
#criando um vetor de espectros
color = ('b', 'g', 'r')
#usando os espectros em um loop para concatenar os gráficos dos espectros
for i,col in enumerate(color):
    hist = cv2.calcHist([img],[i],None , [256], [0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])
plt.show()
#Separa os canais