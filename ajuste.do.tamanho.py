import cv2

img = cv2.imread('teste2.JPG')
scale_percent = 30  #escala da imagem original
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# redimensionando a imagem
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
cv2.imwrite('teste2.JPG', resized)

cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
