import os

from grayscale import grayScale
from reason_growing import regionGrowing
from split import split
from utils.countPixel import countPixel
from utils.gaussFilter import gaussFilter


def processImage(file, exclude, image_path, process_path, grid, thresh, DB):
    if file in exclude:
        return
    print("Processing: " + image_path + "/" + file)
    file_path = image_path + "/" + file
    filename = file.split('.')[0]
    os.makedirs(f'{process_path}/{filename}', 0o777, True)
    record = open(f"./{process_path}/{filename}/record.txt", "a")

    # Define parameters
    vector = []

    # Process image
    gauss_file = process_path + "/" + filename + "/gaussFilter.jpg"
    gaussFilter(f'{file_path}', f'{gauss_file}')
    print(filename + ' gaussFilter done')

    # convert gray level
    gray_file = process_path + "/" + filename + "/gray.jpg"
    grayScale(f'{gauss_file}', f'{gray_file}')
    print(filename + ' grayScale done')

    # Histogram

    # get min, max gray level


    # region growing
    region_growing_file = process_path + "/" + filename + "/regionGrowing.jpg"
    regionGrowing(filename,f'{gray_file}', f'{region_growing_file}', grid, thresh)
    print(filename + ' regionGrowing done')

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

    os.makedirs(f'{process_path}/{filename}/region', 0o777, True)
    split(f'{region_growing_file}', f'{process_path}/{filename}/region', grid)
    print('split region done')

    for i in range(1, grid * grid + 1, 1):
        position = countPixel(f'{process_path}/{filename}/region/part_{i}.jpg')
        if position[1] != 0:
            vector.append(round(position[0] / position[1], 3))
        else:
            vector.append(0)

    record.write(f'{vector}\n')
    record.close()

    DB.write(f'{file} has {vector}\n')