from PIL import Image
import os
def grayScale(source_file, destination_file):
    img = Image.open(source_file).convert('L')
    img.save(destination_file)