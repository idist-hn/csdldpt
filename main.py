import argparse
import shutil
import os
import sys

from utils.threads import processImage

# Parse Params/Options from commandline
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--From", help="Mã file bắt đầu")
parser.add_argument("-t", "--To", help="Mã file kết thúc")
args = parser.parse_args()

if args.From:
    print("Processing file from: % s" % args.From)
else:
    print("From ID can't null")
    sys.exit()

if args.To:
    print("Processing file to: % s" % args.To)
else:
    print("To ID can't null")
    sys.exit()
print("-------------------------------------------------")

# Define parameters
image_path = f'./dataset'
process_path = f'./processed-data'
databases_path = f'./databases'
exclude = ['.git', 'README.md', ".DS_Store"]
grid = 4
thresh = 5

# Reset processed-data folder
# shutil.rmtree(f'./{process_path}', True)
# shutil.rmtree(f'./{databases_path}', True)
os.makedirs(f'./{databases_path}', 0o777, True)

files = os.listdir(f'{image_path}')
files.sort()

for file in files:
    if file in exclude:
        continue
    # get file name
    filename = file.split('.')[0]
    filenameInt = int(filename)
    if filenameInt < int(args.From) or filenameInt > int(args.To):
        continue
    DB = open(f"./databases/vectorData.txt", "a")
    thread = processImage(file, exclude, image_path, process_path, grid, thresh, DB)
    DB.close()
