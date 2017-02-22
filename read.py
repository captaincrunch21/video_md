import allfunctions
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
ima = Image.open('test.jpg')
gray_array=allfunctions.grayscale(ima.load(),ima.size)
gray_array=np.array(gray_array)
# choice=input('l for border,f for face\n')
# filter_array = allfunctions.filter(gray_array)
directed_array=allfunctions.edgedetection(gray_array)
plt.imshow(directed_array,cmap='gray')
plt.show()
# print(gray_array)
# im.show()
