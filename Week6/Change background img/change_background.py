import cv2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

green_background_img = cv2.imread("./Image data/GreenBackground.png", 1)
new_background_img = cv2.imread("./Image data/NewBackground.jpg", 1)
object = cv2.imread("./Image data/Object.png", 1)

IMG_SIZE = (678, 381)
new_background_img = cv2.resize(new_background_img, IMG_SIZE)

print(f"green_shape: {green_background_img.shape}, new_backgound: {new_background_img.shape}, object_shape: {object.shape}")

green_background_img = green_background_img[:,:,::-1]
new_background_img = new_background_img[:,:,::-1]
object = object[:,:,::-1]

result = cv2.absdiff(object,green_background_img)

new_img = np.where(result > 0, object, new_background_img)
plt.imshow(new_img)
plt.show()