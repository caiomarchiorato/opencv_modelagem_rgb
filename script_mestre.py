from os import listdir
import cv2
import numpy as np
import os

def listar_arquivos(caminho=None) :
    lista_arqs = [arq for arq in listdir(caminho)]
    return lista_arqs

if __name__ == '__main__':
    imagens = listar_arquivos(caminho="imagens")

os.chdir("/home/caio/Área de Trabalho/Imagens_pt/imagens")

for imagen in imagens:
    img = cv2.imread(imagen)s
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower3 = (10, 45, 50)
    upper3 = (100, 255, 255)
    mask3 = cv2.inRange(hsv, lower3, upper3)
    res3 = cv2.bitwise_and(img, img, mask=mask3)
    cv2.imwrite(imagen, res3)