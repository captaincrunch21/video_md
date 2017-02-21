import allfunctions
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
ima = Image.open('test.jpg')
gray_array=allfunctions.grayscale(ima.load(),ima.size)
gray_array=np.array(gray_array)
choice=input('l for border,f for face\n')
filter_array = allfunctions.filter(gray_array,choice)
plt.imshow(filter_array,cmap='gray')
plt.show()
# print(gray_array)
# im.show()