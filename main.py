from grayscale import grayScale
from gaussFilter import gaussFilter
from reason_growing import regionGrowing
from split import split
from countPixel import countPixel
import os
import re
import numpy as np
from scipy.spatial import distance


vector = []
euclidDistance = []
vectorImg = []

ROOT_DIR = os.path.abspath(os.curdir)
image_path = f'{ROOT_DIR}/Images'
process_path = f'{ROOT_DIR}/ProcessedImages'
print (ROOT_DIR)
gaussFilter(f'{image_path}/1.jpg')
print('ok')
grayScale(f'{image_path}/1.jpg', f'{process_path}/1/1_gray.jpg')
print('ok')
regionGrowing(f'{image_path}/1.jpg', f'{process_path}/1/1_reason.jpg')
print('ok')
pixel = countPixel(f'{image_path}/1.jpg')
square = pixel[0]/(pixel[1]+1)
print(pixel)
vector.append(square)
split(f'{image_path}/1.jpg')
print('ok')
for i in range(1, 17, 1):
    position = countPixel(f'{process_path}/1/{i}.jpg')
    if position[0]/(position[1] + 1) > 0.4:
        vector.append(1)
    else:
        vector.append(0)
f = open(f"{ROOT_DIR}/vectorData.txt", "a")
f.write(f'{image_path} has {vector}\n')
f.close()

testVector= [0.123, 112, 1, 1, 330, 1, 1, 0, 0, 1, 1, 19834, 0, 1, 1, 1, 1]

with open(f"{ROOT_DIR}/vectorData.txt", 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line.split('has')[1].strip()
        print(line)
        vectorImg = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", line)
        x = np.array(vectorImg)
        savedVector = x.astype(np.float)
        dis = distance.euclidean(savedVector, testVector)
        euclidDistance.append(dis)
        # print(dis)
        # print(savedVector)
        # print(line)
# for i in range(0, euclidDistance.len(), 1):
    # find min and images









