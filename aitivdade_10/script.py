import cv2
import numpy as np


img_color = cv2.imread(r"./img/img.bmp")
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)


edges = cv2.Canny(img_gray, 0, 255)


lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=10, minLineLength=10, maxLineGap=10)


for line in lines:
    x1, y1, x2, y2 = line[0]
    angle = np.abs(np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi)
    if angle < 10 or angle > 80:  
        cv2.line(img_color, (x1, y1), (x2, y2), (0, 255, 0), 2)


cv2.imshow('Linhas Horizontais e Verticais', img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()