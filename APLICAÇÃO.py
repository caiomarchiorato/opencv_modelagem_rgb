import cv2
import numpy as np

#carregando a imagem e convertendo em hsv
img = cv2.imread("219_1_1.JPG")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#determinando limites superiores e inferiores de valores
lower = (10, 120, 100)
upper = (100, 255, 255)

lower2 = (10, 90, 10)
upper2 = (100, 255, 255)

lower3 = (10, 45, 50)
upper3 = (100, 255, 255)

#criando e aplicando as mascaras (cv2.inRange() é usado para calcular as mascaras)
mask = cv2.inRange(hsv, lower, upper)
mask2 = cv2.inRange(hsv, lower2, upper2)
mask3 = cv2.inRange(hsv, lower3, upper3)

res = cv2.bitwise_and(img, img, mask=mask)
res2 = cv2.bitwise_and(img, img, mask=mask2)
res3 = cv2.bitwise_and(img, img, mask=mask3)

numpy_horizontal_concat = np.concatenate((res, img), axis=1)
numpy_horizontal_concat2 = np.concatenate((res2, img), axis=1)
numpy_horizontal_concat3 = np.concatenate((res3, img), axis=1)

#cv2.imwrite('Mask1.JPEG', numpy_horizontal_concat); cv2.imwrite('Mask2.JPEG', numpy_horizontal_concat2); cv2.imwrite('Mask3.JPEG', numpy_horizontal_concat3)

cv2.imshow("GREEN", numpy_horizontal_concat);cv2.imshow("GREEN2", numpy_horizontal_concat2);cv2.imshow("GREEN3", numpy_horizontal_concat3);cv2.waitKey();cv2.destroyAllWindows()

#Além disso, esse espaço de cor permite um elevado grau de separação entre cor e iluminação, o que o qualifica para ser utilizado em diversas técnicas de processamento de imagens.

cv2.imwrite("Mascara.JPEG", numpy_horizontal_concat3)