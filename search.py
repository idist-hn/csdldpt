import argparse
import os.path
import sys
import re
import cv2 as cv
from matplotlib import pyplot as plt
from scipy.spatial import distance
import numpy as np

from utils.threads import processImage

# Declare variables
file_path = ""
file = ""
filename = ""
grid = 4
thresh = 5
process_path = "search-sources"
sameThresh = 100


class ImageCompare():  # leave this empty
    def __init__(self):  # constructor function using self
        self.Filename = ""  # variable using self.
        self.Distance = 9999999  # variable using self
        self.DistanceHistogram = 9999999  # variable using self

    def str(self):
        return f'{self.Filename} => euclid: {self.Distance}, histogram: {self.DistanceHistogram}'


# Parse Params/Options from commandline
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--File", help="File path cần tìm kiếm")
args = parser.parse_args()

if args.File:
    print("Processing file: % s" % args.File)
    file = os.path.basename(args.File)
    file_path = os.path.dirname(args.File)
    filename = os.path.splitext(file)[0]
else:
    print("File path can't null")
    sys.exit()

# Check file tồn tại hay không
if os.path.isfile(f'{file_path}/{file}') == False:
    print(f'{file_path}/{file} is not exist!')
    sys.exit()

# Process file, tính vector
searchVector = open(f"./databases/vectorSearch.txt", "w")
processImage(file, "", file_path, process_path, grid, thresh, searchVector)
searchVector.close()

# Read result
result = open(f"./databases/vectorSearch.txt", "r")
searchVectorHistogram = open(f"./search-sources/{filename}/histogram.jpg_vector.txt", "r")
with result as record:
    while True:
        searchRecord = record.readline()
        if not searchRecord:
            break
        searchRecord = searchRecord.split('has')[1].strip()
        searchLine = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", searchRecord)
        searchArray = np.array(searchLine)
        searchVector = searchArray.astype(np.float64)
result.close()

euclidDistances = []
# Read database:
DB = open(f"./databases/vectorData.txt", "r")
with DB as row:
    while True:
        line = row.readline()
        if not line:
            break
        fileScan = line.split('has')[0].strip()
        line = line.split('has')[1].strip()
        vectorImg = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", line)
        # imageFile = re.findall(r".+\.jpg", line)
        # print(f'Processing: {imageFile}')
        x = np.array(vectorImg)
        savedVector = x.astype(np.float64)
        dis = distance.euclidean(savedVector, searchVector)
        disHistogram = distance.euclidean(savedVector, searchVector)
        imageCompare = ImageCompare()
        imageCompare.Distance = round(dis, 3)
        imageCompare.DistanceHistogram = round(disHistogram, 3)
        imageCompare.Filename = fileScan

        if imageCompare.Distance > sameThresh:
            continue
        euclidDistances.append(imageCompare)
DB.close()

# Find 3 min distance image
euclidDistances.sort(key=lambda x: x.Distance, reverse=False)

# xoá các phần tử có giá trị Distance = 0
euclidDistances = [x for x in euclidDistances if x.Distance != 0]

imgSource = cv.imread(f'{file_path}/{file}')
plt.subplot(221), plt.imshow(imgSource), plt.title(f'Image Search')
plt.xticks([]), plt.yticks([])

if len(euclidDistances) > 2:
    img3 = cv.imread(f'dataset/{euclidDistances[2].Filename}')
    plt.subplot(224), plt.imshow(img3), plt.title(f'Image Result 3: {euclidDistances[2].Filename} => {euclidDistances[2].Distance}')
    plt.xticks([]), plt.yticks([])

if len(euclidDistances) > 1:
    img2 = cv.imread(f'dataset/{euclidDistances[1].Filename}')
    plt.subplot(223), plt.imshow(img2), plt.title(f'Image Result 2: {euclidDistances[1].Filename} => {euclidDistances[1].Distance}')
    plt.xticks([]), plt.yticks([])

if len(euclidDistances) > 0:
    img1 = cv.imread(f'dataset/{euclidDistances[0].Filename}')
    plt.subplot(222), plt.imshow(img1), plt.title(f'Image Result 1: {euclidDistances[0].Filename} => {euclidDistances[0].Distance}')
    plt.xticks([]), plt.yticks([])

plt.show()
