import numpy as np
import cv2

img = cv2.imread("milho.jpg")
img_gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#sobelx = cv2.Sobelimg, cv2.CV_64F, 1, 0)
#sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)
#sobelx = np.uint8(np.absolute(sobelx))
#sobely = np.uint8(np.absolute(sobely))
#sobel = cv2.bitwise_or(sobelx, sobely)

#result = np.vstack([np.hstack([img, sobelx]), 
#                    np.hstack([sobely, sobel])
#                    ])

#cv2.imshow("Sobel", result)
#cv2.waitKey(0)



suave = cv2.GaussianBlur(img_gs, (3,3), 0)

canny1 = cv2.Canny(suave, 20, 120)
canny2 = cv2.Canny(suave, 70, 200)

original = cv2.bitwise_and(img, img, mask = canny2)

cv2.imshow("Detector Canny", original
           )
cv2.waitKey(0)
