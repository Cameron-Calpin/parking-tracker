import numpy as np
import scipy
import scipy.signal as sig
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.feature import hog

im = cv2.imread('test4.jpg')
img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
print(img.shape)
# img = mpimg.imread('test4.jpg')
# plt.imshow(img)
# plt.show()

# # Define the Sobel operator kernels.
# kernel_x = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
# kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

# G_x = sig.convolve2d(img, kernel_x, mode='same') 
# G_y = sig.convolve2d(img, kernel_y, mode='same') 

# # Plot them!
# fig = plt.figure()
# ax1 = fig.add_subplot(121)
# ax2 = fig.add_subplot(122)

# # Actually plt.imshow() can handle the value scale well even if I don't do 
# # the transformation (G_x + 255) / 2.
# ax1.imshow((G_x + 255) / 2, cmap='gray'); ax1.set_xlabel("Gx")
# ax2.imshow((G_y + 255) / 2, cmap='gray'); ax2.set_xlabel("Gy")
# plt.show()

'''
Using skimage
'''
fd, hog_img = hog(img, orientations=9, pixels_per_cell=(8, 8),
        cells_per_block=(3, 3), transform_sqrt=False, 
        visualize=True, feature_vector=True)
plt.imshow(hog_img)
plt.show()


# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV);
# cv2.imshow('hsv', hsv)
# cv2.waitKey()