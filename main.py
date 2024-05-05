import shutil

from grayscale import grayScale
from gaussFilter import gaussFilter
from reason_growing import regionGrowing
from split import split
from countPixel import countPixel
import os
import re
import numpy as np
from scipy.spatial import distance

# Define parameters
image_path = f'./init-sources'
process_path = f'./processed-data'
databases_path = f'./databases'
grid = 4

# Reset processed-data folder
shutil.rmtree(f'./{process_path}')
shutil.rmtree(f'./{databases_path}')
os.makedirs(f'./{databases_path}', 0o777, True)

files = os.listdir(f'{image_path}')
DB = open(f"./databases/vectorData.txt", "a")

for file in files:
    print("Processing: " + image_path + "/" + file)
    file_path = image_path + "/" + file
    filename = file.split('.')[0]
    os.makedirs(f'{process_path}/{filename}', 0o777, True)
    record = open(f"./{process_path}/{filename}/record.txt", "a")

    # Define parameters
    vector = []
    euclidDistance = []
    vectorImg = []

    # Process image
    gauss_file = process_path + "/" + filename + "/gaussFilter.jpg"
    gaussFilter(f'{file_path}', f'{gauss_file}')
    print('gaussFilter done')

    gray_file = process_path + "/" + filename + "/gray.jpg"
    grayScale(f'{gauss_file}', f'{gray_file}')
    print('grayScale done')

    region_growing_file = process_path + "/" + filename + "/regionGrowing.jpg"
    regionGrowing(f'{gray_file}', f'{region_growing_file}', grid)
    print('regionGrowing done')

    pixel = countPixel(f'{region_growing_file}')
    square = pixel[0] / (pixel[1] + 1)
    vector.append(round(square,3))

    os.makedirs(f'{process_path}/{filename}/gauss/', 0o777, True)
    split(f'{gauss_file}', f'{process_path}/{filename}/gauss', grid)
    print('split gauss done')

    for i in range(1, grid * grid + 1, 1):
        position = countPixel(f'{process_path}/{filename}/gauss/part_{i}.jpg')
        if position[1] != 0:
            vector.append(round(position[0] / position[1], 3))
        else:
            vector.append(0)

    os.makedirs(f'{process_path}/{filename}/gray', 0o777, True)
    split(f'{gray_file}', f'{process_path}/{filename}/gray', grid)
    print('split gray done')

    for i in range(1, grid * grid + 1, 1):
        position = countPixel(f'{process_path}/{filename}/gray/part_{i}.jpg')
        if position[1] != 0:
            vector.append(round(position[0] / position[1], 3))
        else:
            vector.append(0)
    record.write(f'{vector}\n')
    record.close()

    DB.write(f'{file_path} has {vector}\n')

DB.close()

# testVector= [0.123, 112, 1, 1, 330, 1, 1, 0, 0, 1, 1, 19834, 0, 1, 1, 1, 1]
#
# with open(f"{ROOT_DIR}/vectorData.txt", 'r') as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         line = line.split('has')[1].strip()
#         print(line)
#         vectorImg = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", line)
#         x = np.array(vectorImg)
#         savedVector = x.astype(np.float64)
#         dis = distance.euclidean(savedVector, testVector)
#         euclidDistance.append(dis)
#         # print(dis)
#         # print(savedVector)
#         # print(line)
# # for i in range(0, euclidDistance.len(), 1):
#     # find min and images
#
#
#
