import cv2
import os


def split(source_file, destination_folder, grid):
    img = cv2.imread(source_file)
    name = 1
    height = img.shape[0]
    width = img.shape[1]
    for r in range(0, height, round(height / grid) + 1):
        for c in range(0, width, round(width / grid) + 1):
            cv2.imwrite(f'{destination_folder}/part_{name}.jpg',
                        img[r:r + round(height / grid) + 1, c:c + round(width / grid) + 1:])
            name += 1
    return
