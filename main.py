import shutil
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
    thread = processImage(file, exclude, image_path, process_path, grid, thresh, DB)
    DB.close()






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
