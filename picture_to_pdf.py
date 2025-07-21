# TODO (not implemented yet)
import os
from PIL import Image

folder_path = r"test_path\tests\test"  # change this
out_path = r"test_path\tests\test\output.pdf"

pictures_list = []

for filename in os.listdir(folder_path):
    if filename.endswith('.png') or filename.endswith('.jpg'):
        picture_path = os.path.join(folder_path, filename)
        picture = Image.open(picture_path).convert('RGB')
        pictures_list.append(picture)

if pictures_list:
    base_picture = pictures_list[0]
    del pictures_list[0]
    base_picture.save(out_path, save_all=True, append_images=pictures_list)
