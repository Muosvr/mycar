import numpy as np

class ImageArrays:
    def __init__(self):
        tmp = np.zeros((120, 160, 3))
        self.images = [tmp for i in range(3)]
        # self.images = [[0, 0, 0],
        #                [0, 0, 0],
        #                [0, 0, 0]]
    def run(self, image):
        self.images.pop(0)
        self.images.append(image)
        return self.images
pic = np.random.rand(120, 160, 3)
img_arr = ImageArrays()
# print(img_arr.images)
img_arr.run(pic)
print(np.array(img_arr.images).shape)
