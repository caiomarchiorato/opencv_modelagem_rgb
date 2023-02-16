import glob
import cv2

path = glob.glob("imagens/*.jpg")
cv_img = []
for img in path:
    n = cv2.imread(img)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower3 = (10, 45, 50)
    upper3 = (100, 255, 255)
    mask3 = cv2.inRange(hsv, lower3, upper3)
    res3 = cv2.bitwise_and(img, img, mask=mask3)
    cv2.imwrite(img, res3)
    cv_img.append(n)
