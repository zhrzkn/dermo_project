import cv2
import numpy as np
img = cv2.imread("dosya_adi.jpg", 0)
laplacian = cv2.Laplacian(img, cv2.CV_64F)
cv2.imshow("pencere", laplacian)
cv2.imwrite("yeni_dosya.png", laplacian)                
cv2.waitKey(0)
cv2.destroyAllWindows()