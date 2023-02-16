import cv2
import numpy as np

img = cv2.imread("219_1_1.JPG")
roi = img[2128:2128+200, 1624:1624+200]

cv2.imshow("Area de interesse", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(len(roi))
print(roi.shape)
print(roi.size)