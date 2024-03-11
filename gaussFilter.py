import cv2 as cv
import os
from matplotlib import pyplot as plt

def gaussFilter(path):
    img = cv.imread(path)
    imgName = os.path.basename(path)
    imgName = imgName.split('.')[0]
    # Convert color from bgr (OpenCV default) to rgb
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    blur2 = cv.blur(img, (2, 2))
    median = cv.cvtColor(blur2, cv.COLOR_BGR2RGB)
    cv.imwrite(f'{imgName}_median.jpg', median)
