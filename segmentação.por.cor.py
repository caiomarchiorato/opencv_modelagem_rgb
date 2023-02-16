import cv2
import numpy as np

def filtroRGB(src, r, g, b):
    if r == 0:
        src[:, :, 2] = 0
    if g == 0:
        src[:, :, 1] = 0
    if b == 0:
        src[:, :, 0] = 0

def show_image():
    filtro = 1

    while True:
        img = cv2.imread('DSCF5539dois.JPG')
        if filtro == 1:
            cv2.imshow('Imagem', img)

        if filtro == 2:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Imagem', gray)
        if filtro == 6:
            filtroRGB(img, 1, 0, 0)
            cv2.imshow('OpenCV filtro', img)
        if filtro == 7:
            filtroRGB(img, 0, 1, 0)
            cv2.imshow('OpenCV filtro', img)
        if filtro == 8:
            filtroRGB(img, 0, 0, 1)
            cv2.imshow('Open CV filtro', img)

        ret = cv2.waitKey(1)
        if ret == 27:
            break
        elif ret == -1:
            continue
        elif ret == 49:
            filtro = 1
        elif ret == 50:
            filtro = 2
        elif ret == 54:
            filtro = 6
        elif ret == 55:
            filtro = 7
        elif ret == 56:
            filtro = 8

cv2.destroyAllWindows()

def main():
    show_image()
    return 0

if __name__ == '__main__':
    main()