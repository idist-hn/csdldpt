import os
from PIL import Image

def resize_image(image_path, output_path, size):
    with Image.open(image_path) as image:
        # Tính toán tỷ lệ ban đầu
        original_ratio = image.width / image.height

        # Tính toán kích thước mới dựa trên tỷ lệ ban đầu và kích thước mong muốn
        if original_ratio > 1:
            new_size = (int(size * original_ratio), size)
        else:
            new_size = (size, int(size / original_ratio))

        # Thay đổi kích thước ảnh
        resized_image = image.resize(new_size)

        # Cắt ảnh để có tỉ lệ 1:1
        left = (resized_image.width - size) / 2
        top = (resized_image.height - size) / 2
        right = (resized_image.width + size) / 2
        bottom = (resized_image.height + size) / 2
        cropped_image = resized_image.crop((left, top, right, bottom))

        print('Done pic no: ' + image_path)
        cropped_image.save(output_path)


exclude = ['.git', 'README.md', ".DS_Store"]
# get list folder exclude .git
list_folder = os.listdir('./data-sources')

os.makedirs("init-sources", 0o777, True)
for folder in list_folder:
    if folder in exclude:
        continue

    files = os.listdir(f'./data-sources/{folder}')
    for file in files:
        print(file)
        image_path = f"./data-sources/{folder}/{file}"
        output_path = f"./init-sources/{folder}_{file}"
        resize_image(image_path, output_path, 500)
