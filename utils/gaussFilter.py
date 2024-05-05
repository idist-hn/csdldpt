import cv2 as cv
import os
from matplotlib import pyplot as plt


def gaussFilter(source_file, destination_file):
    img = cv.imread(source_file)
    # Convert color from bgr (OpenCV default) to rgb
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    blur = cv.blur(img_rgb, (2, 2))
    median = cv.cvtColor(blur, cv.COLOR_BGR2RGB)
    cv.imwrite(f'{destination_file}', median)
