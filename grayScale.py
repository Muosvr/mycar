import numpy as np
from PIL import Image

def gray_scale(image_array):
    img = Image.fromarray(image_array)
    img = img.convert("L")
    img_array = np.array(img).reshape(120, 160, 1)
    return img_array

pic = np.random.rand(120, 160, 3)*255
pic = pic.astype('uint8')
array = gray_scale(pic)

print("Previous shape:", pic.shape)
print("Shape now:" , array.shape)
