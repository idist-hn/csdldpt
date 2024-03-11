import cv2
import os
# 640*360 -> split 4x4 -> 160x90
def split(path):
    ROOT_DIR = os.path.abspath(os.curdir)
    print(ROOT_DIR)
    img = cv2.imread(path)
    imgName = os.path.basename(path)
    imgName = imgName.split('.')[0]
    name = 1
    dir = f'{ROOT_DIR}'
    isExist = os.path.exists(dir)
    if not isExist:
        os.makedirs(dir)
        print("The new directory is created!")
    os.chdir(dir)

    height = img.shape[0]
    width = img.shape[1]
    print (width, height, width/4)
    print('ok')

    for r in range(0,height,round(height/4)+1):
        for c in range(0,width,round(width/4)+1):
            cv2.imwrite(f'{dir}/{name}.jpg',img[r:r+round(height/4)+1, c:c+round(width/4)+1:])
            name += 1
    return
