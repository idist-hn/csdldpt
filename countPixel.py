import cv2
import numpy as np

def countPixel(path):
    # reading the image data from desired directory
    img = cv2.imread(path)
    # cv2.imshow('Image', img)
    # counting the number of pixels
    number_of_white_pix = np.sum(img > 128)
    number_of_black_pix = np.sum(img <= 128)
    pixel = number_of_black_pix, number_of_white_pix
    return pixel