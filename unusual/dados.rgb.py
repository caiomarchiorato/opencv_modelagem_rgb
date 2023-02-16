import cv2
import numpy as np
from matplotlib import pyplot as plt


img =  cv2.imread("Imagem.JPEG", 1)
img_gray = cv2.imread('DSCF4385.JPG', 0)

#calculando valor médio dos pixels
valorMedio = cv2.mean(img)
valorMedioGray = cv2.mean(img_gray)

#calculando média e desvio  padrão  dos pixels
(mean, std) = cv2.meanStdDev(img)
(means, stds) = cv2.meanStdDev(img_gray)

#juntando as informações
RGB = np.concatenate([(mean, std)]).flatten()
Gray = np.concatenate([(means, stds)]).flatten()

print('Valores da média e desvio padrão RGB')
print(valorMedio)
print(RGB)

print('Valores da média e desvio padrão Escalas de cinza')
print(valorMedioGray)
print(Gray)