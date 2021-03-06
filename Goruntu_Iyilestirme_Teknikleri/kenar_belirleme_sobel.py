import cv2
import numpy as np
img = cv2.imread("dosya_adi.jpg", 0)
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=1)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=1)
edges_sobel = np.hypot(sobel_x, sobel_y)
edges_sobel *= 700.0 / np.max(edges_sobel)
cv2.imshow("pencere", edges_sobel)
cv2.imwrite("yeni_dosya.png", edges_sobel)                                     
cv2.waitKey(0)
cv2.destroyAllWindows()