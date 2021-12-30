import os
import re
import json
import traceback
from datetime import date, datetime
from pprint import pprint
from PIL import Image
import numpy as np
from copy import copy
#
# GREYSCALE = False
#
# def get_new_val(old_val, nc):
#     """
#     Get the "closest" colour to old_val in the range [0,1] per channel divided
#     into nc values.
#
#     """
#
#     return np.round(old_val * (nc - 1)) / (nc - 1)
#
# # For RGB images, the following might give better colour-matching.
# #p = np.linspace(0, 1, nc)
# #p = np.array(list(product(p,p,p)))
# #def get_new_val(old_val):
# #    idx = np.argmin(np.sum((old_val[None,:] - p)**2, axis=1))
# #    return p[idx]
#
# def fs_dither(img, nc):
#     """
#     Floyd-Steinberg dither the image img into a palette with nc colours per
#     channel.
#
#     """
#
#     arr = np.array(img, dtype=float) / 255
#
#     for ir in range(new_height):
#         for ic in range(new_width):
#             # NB need to copy here for RGB arrays otherwise err will be (0,0,0)!
#             old_val = arr[ir, ic].copy()
#             new_val = get_new_val(old_val, nc)
#             arr[ir, ic] = new_val
#             err = old_val - new_val
#             # In this simple example, we will just ignore the border pixels.
#             if ic < new_width - 1:
#                 arr[ir, ic+1] += err * 7/16
#             if ir < new_height - 1:
#                 if ic > 0:
#                     arr[ir+1, ic-1] += err * 3/16
#                 arr[ir+1, ic] += err * 5/16
#                 if ic < new_width - 1:
#                     arr[ir+1, ic+1] += err / 16
#
#     carr = np.array(arr/np.max(arr, axis=(0,1)) * 255, dtype=np.uint8)
#     return Image.fromarray(carr)
#
#
# def palette_reduce(img, nc):
#     """Simple palette reduction without dithering."""
#     arr = np.array(img, dtype=float) / 255
#     arr = get_new_val(arr, nc)
#
#     carr = np.array(arr/np.max(arr) * 255, dtype=np.uint8)
#     return Image.fromarray(carr)
#
#
# def remove_camel(word):
#     new_name = word.replace(" ", "_")
#     new_name = new_name.replace("-", "")
#     new_name = new_name.replace("+", "")
#     new_name = re.sub(r'((?<=[a-z])[A-Z]|[A-Z](?=[a-z]))', r'_\1', new_name)
#     if new_name[0] == "_":
#         new_name = new_name[1:]
#     new_name = new_name.lower()
#     new_name = re.sub(r'(_+)', r'_', new_name)
#
#     return new_name
#
#
# # def dither_matrix(n:int):
# #     if n == 1:
# #         return np.array([[0]])
# #     else:
# #         first = (n ** 2) * dither_matrix(int(n/2))
# #         second = (n ** 2) * dither_matrix(int(n/2)) + 2
# #         third = (n ** 2) * dither_matrix(int(n/2)) + 3
# #         fourth = (n ** 2) * dither_matrix(int(n/2)) + 1
# #         first_col = np.concatenate((first, third), axis=0)
# #         second_col = np.concatenate((second, fourth), axis=0)
# #         return (1/n**2) * np.concatenate((first_col, second_col), axis=1)
# #
# # def get_image(src:str):
# #     img = np.array(Image.open(src))
# #     img_arr = [[(j[0] * 299/1000) + (j[1] * 587/1000) + (j[2] * 114/1000) for j in r] for r in img]
# #     img_gray = np.array(img_arr)
# #     # Image.fromarray(img_gray).convert('L').save('gray-scale.png')
# #
# #     return img_gray * (1/255)
# #
# # def ordered_dithering(img_pixel:np.array, dither_m:np.array, src):
# #     n = np.size(dither_m, axis=0)
# #     x_max = np.size(img_pixel, axis=1)
# #     y_max = np.size(img_pixel, axis=0)
# #     for x in range(x_max):
# #         for y in range(y_max):
# #             i = x % n
# #             j = y % n
# #             if img_pixel[y][x] > dither_m[i][j]:
# #                 img_pixel[y][x] = 255
# #             else:
# #                 img_pixel[y][x] = 0
# #
# #     parts = src.split("/")
# #     src = "/".join(parts[:-1]) + '/dithered_' + parts[-1].split(".")[0] + ".png"
# #     Image.fromarray(img_pixel).convert('L').save(src, bit=1)
# #
# #     return src
#
def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))


with open('src/items.json', 'r') as dataset:
    c = dataset.read()
    items = json.loads(c)

with open('src/dataset.json', 'r') as dataset:
    c = dataset.read()
    projects = json.loads(c)

projects = {x['name']: x['date'] for x in projects}
md_list = []

with open('src/dataset.json', 'w') as dataset:

    for filename in os.listdir("md"):
        if '.md' in filename:
            md_dict = {}
            with open(os.path.join("md", filename), 'r') as f:
                contents = f.read()
                filename = filename.split('.md')[0]

                md_dict['name'] = filename
                md_dict['contents'] = contents
                md_dict['date'] = datetime.now() if filename not in list(projects.keys()) else projects[filename]

                md_list.append(md_dict)

    dataset.write(json.dumps(md_list, default=json_serial))

print("python file ran")
#
#
# with open('src/items_2.json', 'w') as dataset:
#     n = 100
#     for item in items:
#         # item['name'] = remove_camel(item['name'])
#
#         # new_images = []
#         for i in range(len(item['image'])):
#             # image = item['image'][i]
#             # new_src = remove_camel(image)
#             # image = 'public/images/' + item['image'][i]
#             # new_src = f"public/images/{new_src}"
#             # try:
#             #     os.rename(image, new_src)
#             # except:
#             #     print(traceback.format_exc())
#             #
#             # new_images.append(remove_camel(image))
#             if i == 0:
#                 new_src = item['image'][0]
#                 if new_src[0] == "_":
#                     new_src = new_src[1:]
#                 new_src = f"public/images/{new_src}"
#
#
#                 img = Image.open(new_src)
#                 if GREYSCALE:
#                     img = img.convert('L')
#
#                 width, height = img.size
#                 new_width = 400
#                 new_height = int(height * new_width / width)
#                 img = img.resize((new_width, new_height), Image.ANTIALIAS)
#
#                 nc = 2
#                 parts = new_src.split("/")
#                 src = "/".join(parts[:-1]) + '/dithered_' + parts[-1].split(".")[0] + ".png"
#
#                 dim = fs_dither(img, nc)
#                 dim.save(src.format(nc))
#
#                 # rim = palette_reduce(img, nc)
#                 # rim.save('rimg-{}.jpg'.format(nc))
#
#         # item['image'] = new_images
#         # item['dithered'] = src
#
#
#     dataset.write(json.dumps(items, default=json_serial))
