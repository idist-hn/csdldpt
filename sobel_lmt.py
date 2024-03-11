import cv2
import numpy as np

for i in range(1, 10):
    img = cv2.imread(str(i) + '.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(float)

    Edge_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    Edge_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    Edge = np.sqrt(Edge_x ** 2 + Edge_y ** 2)  # image can be normalized to
    # fit into 0..255 color space
    cv2.imencode('.jpg', Edge)[1].tofile("Sobel 2 trục - Ảnh " + str(i) + '.jpg')
    cv2.imencode('.jpg', Edge_x)[1].tofile("Sobel trục x - Ảnh " + str(i) + '.jpg')
    cv2.imencode('.jpg', Edge_y)[1].tofile("Sobel trục y - Ảnh " + str(i) + '.jpg')