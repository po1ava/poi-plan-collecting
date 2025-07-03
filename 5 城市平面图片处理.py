import os
from PIL import Image

'''
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''

if __name__ == '__main__':
    directory = '4 城市平面图片/0'
    new_directory = '5 处理后图片'

    result = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith("a.png"):
                result.append(os.path.join(root, file))

    for i in result:
        image = Image.open(i)
        image.thumbnail((256, 256))

        image_a = Image.open(i.replace('_a.png', '_b.png'))
        image_a.thumbnail((256, 256))

        result_image = Image.new("RGB", (512, 256))
        result_image.paste(image, (256, 0))
        result_image.paste(image_a, (0, 0))

        if not os.path.exists(new_directory):
            os.makedirs(new_directory, exist_ok=True)
        result_image.save(i.replace('_a.png', '_.png').replace(directory, new_directory))
