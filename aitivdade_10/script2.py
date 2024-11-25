import cv2
import numpy as np


img_color = cv2.imread(r"./img/img.bmp")
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(img_gray, (9, 9), 2)
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=10, maxRadius=100)


if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])  
        radius = i[2]         
        cv2.circle(img_color, center, radius, (255, 0, 0), 2)  
        cv2.circle(img_color, center, 2, (0, 0, 255), 3)       


cv2.imshow('Círculos Detectados', img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()