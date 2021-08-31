import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("152.png")
b, g, r = cv2.split(img)

plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])
plt.show()
cv2.imwrite("histogram_152.png", r)
cv2.waitKey(0)
cv2.destroyAllWindows()