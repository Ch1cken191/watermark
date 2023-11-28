import cv2
from PIL import Image
import numpy as np

import matplotlib.pyplot as plt

#file = "watermarked_image.png"
#file = "extract.png"
file = "image//"
img = cv2.imread(file,0)
cv2.imshow("anh",img)
cv2.waitKey()

hist = np.zeros((265,),np.uint8)

[w,h] = img.shape[:2]

for i in range(w):

    for j in range(h):
        hist[img[i][j]] +=1
fig = plt.figure()
plt.plot(hist)
plt.show()