import cv2
import numpy as np

img = cv2.imread("teste1.JPG")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#definindo limites superiores e inferiores
lower2 = (10, 90, 10)
upper2 = (100, 255, 255)

#criando as mascaras
mask2 = cv2.inRange(hsv, lower2, upper2)
res = cv2.bitwise_and(img, img, mask=mask2)

valorMedio = cv2.mean(res)

(mean, std) = cv2.meanStdDev(res)

RGB = np.concatenate([(mean, std)]).flatten()

cv2.imshow('Res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('Valores da média e desvio padrão RGB')
print(valorMedio)
print(RGB)