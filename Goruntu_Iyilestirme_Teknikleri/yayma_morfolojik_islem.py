import cv2
import numpy as np
img = cv2.imread("dosya_adi.jpg", 0)

kernel = np.ones((5,5),np.uint8)

yayma = cv2.erode(img,kernel,iterations = -1)
cv2.imshow("Pencere", yayma)
cv2.imwrite("yeni_dosya.png", yayma)
cv2.waitKey(0)
cv2.destroyAllWindows()