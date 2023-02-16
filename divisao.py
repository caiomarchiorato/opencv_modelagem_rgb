import cv2
import numpy as np

# Read the image
img = cv2.imread("IMD015.png")
width = img.shape

# Cut the image in half
width_cutoff = width / 2
s1 = img[:, width_cutoff]
s2 = img[:, width_cutoff:]

# Save each half
cv2.imsave("face1.png", s1)
cv2.imsave("face2.png", s2)

i1 = cv2.imread("face1.png")
i2 = cv2.imread("face2.png")
assert i1.mode == i2.mode, "Different kinds of images."
assert i1.size == i2.size, "Different sizes."

pairs = zip(i1.getdata(), i2.getdata())
if len(i1.getbands()) == 1:
    # for gray-scale jpegs
    dif = sum(abs(p1-p2) for p1,p2 in pairs)
else:
    dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))

ncomponents = i1.size[0] * i1.size[1] * 3
print ("Difference (percentage):"+ str((dif / 255.0 * 100) / ncomponents))