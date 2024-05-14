from PIL import Image


# documentation: https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
def grayScale(source_file, destination_file):
    img = Image.open(source_file).convert('L')
    img.save(destination_file)
