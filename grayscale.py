from PIL import Image
import os
def grayScale(path, savePath):
    ROOT_DIR = os.path.abspath(os.curdir)
    imgName = os.path.basename(path)
    imgName = imgName.split('.')[0]
    dir = f'{ROOT_DIR}/ProcessedImages/{imgName}'
    isExist = os.path.exists(dir)
    if not isExist:
        os.makedirs(dir)
        print("The new directory is created!")
    os.chdir(dir)
    img = Image.open(path).convert('L')
    img.save(savePath)