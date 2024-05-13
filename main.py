import shutil
import threading

from grayscale import grayScale
from utils.gaussFilter import gaussFilter
from reason_growing import regionGrowing
from split import split
from utils.countPixel import countPixel
import os

from utils.threads import processImage

# Define parameters
image_path = f'./dataset'
process_path = f'./processed-data'
databases_path = f'./databases'
exclude = ['.git', 'README.md', ".DS_Store"]
grid = 4
thresh = 5

# Reset processed-data folder
shutil.rmtree(f'./{process_path}', True)
shutil.rmtree(f'./{databases_path}', True)
os.makedirs(f'./{databases_path}', 0o777, True)

files = os.listdir(f'{image_path}')
files.sort()

for file in files:
    DB = open(f"./databases/vectorData.txt", "a")
    # thread = threading.Thread(target=processImage, args=(file, exclude, image_path, process_path, grid, thresh, DB))
    thread = processImage(file, exclude, image_path, process_path, grid, thresh, DB)
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
