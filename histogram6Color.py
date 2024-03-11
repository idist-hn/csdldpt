import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image
import math
def histogram(path):
    # reading the image data from desired directory
    img = Image.open(path)
    im = cv2.imread(path)
    # creating a image object
    px = img.load()
    height = im.shape[0]
    width = im.shape[1]
    colorHistogram = [0,0,0,0,0,0]
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    orange = (255, 165, 0)
    purple = (128, 0, 128)
    for col in range(0,height,1):
        for row in range(0,width,1):
            euclidVal = [0, 0, 0, 0, 0, 0];
            euclidMinVal = 0;
            color = 0;
            coordinate = x, y = row, col
            dot = img.getpixel(coordinate)
            euclidVal[0] = math.sqrt( (dot[0]-red[0])*(dot[0]-red[0])+ (dot[1]-red[1])*(dot[1]-red[1]) + (dot[2]-red[2])*(dot[2]-red[2]) )
            euclidVal[1] = math.sqrt( (dot[0]-green[0])*(dot[0]-green[0])+ (dot[1]-green[1])*(dot[1]-green[1]) + (dot[2]-green[2])*(dot[2]-green[2]) )
            euclidVal[2] = math.sqrt( (dot[0]-blue[0])*(dot[0]-blue[0])+ (dot[1]-blue[1])*(dot[1]-blue[1]) + (dot[2]-blue[2])*(dot[2]-blue[2]) )
            euclidVal[3] = math.sqrt( (dot[0]-yellow[0])*(dot[0]-yellow[0])+ (dot[1]-yellow[1])*(dot[1]-yellow[1]) + (dot[2]-yellow[2])*(dot[2]-yellow[2]) )
            euclidVal[4] = math.sqrt( (dot[0]-orange[0])*(dot[0]-orange[0])+ (dot[1]-orange[1])*(dot[1]-orange[1]) + (dot[2]-orange[2])*(dot[2]-orange[2]) )
            euclidVal[5] = math.sqrt( (dot[0]-purple[0])*(dot[0]-purple[0])+ (dot[1]-purple[1])*(dot[1]-purple[1]) + (dot[2]-purple[2])*(dot[2]-purple[2]) )

            euclidMinVal = euclidVal[0]
            for loop in range(0, 6, 1):
                if euclidMinVal > euclidVal[loop]:
                    euclidMinVal = euclidVal[loop]
                    color = loop
            colorHistogram[color] = colorHistogram[color] + 1

    return colorHistogram





    # print(im.getpixel(coordinate));