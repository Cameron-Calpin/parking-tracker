import numpy as np
import cv2
import matplotlib.pyplot as plt
import glob
import time

orient = 9
x_pix_per_cell = 128
y_pix_per_cell = 72
cell_per_block = 4

image = cv2.imread('test4.jpg')

img = image.astype(np.float32) / 255
img_shape = img.shape
print(img_shape)

nxblocks = (img.shape[1] // x_pix_per_cell) #- 1
nyblocks = (img.shape[0] // y_pix_per_cell) #- 1
nfeat_per_block = orient * cell_per_block ** 2
print("nfeat_per_block:", nfeat_per_block)
print("nxblocks:", nxblocks)
print("nyblocks:", nyblocks)

x_window = 128 * 2
y_window = 72 * 2
x_nblocks_per_window = (x_window // x_pix_per_cell) #- 1
y_nblocks_per_window = (y_window // y_pix_per_cell)

cells_per_step = 1
# nxsteps = (nxblocks - x_nblocks_per_window) // cells_per_step
# nysteps = (nyblocks - y_nblocks_per_window) // cells_per_step
nxsteps = nxblocks
nysteps = nyblocks
print("x_nblocks_per_window:", x_nblocks_per_window)
print("y_nblocks_per_window:", y_nblocks_per_window)
print("nxsteps:", nxsteps)
print("nysteps:", nysteps)

nxblocks_it = 0
nyblocks_it = 0
for i in range(10):
	nyblocks_jump = nyblocks_it + y_pix_per_cell
	for j in range(10):
		nxblocks_jump = nxblocks_it + x_pix_per_cell
		cv2.rectangle(image,(nxblocks_it, nyblocks_it),(nxblocks_jump, nyblocks_jump),(0,0,255),3)
		nxblocks_it = nxblocks_it + x_pix_per_cell
	nxblocks_it = 0
	nyblocks_it = nyblocks_it + y_pix_per_cell


xppc = x_pix_per_cell * 2
yppc = y_pix_per_cell * 2
reg_nxblocks_it = 0
reg_nyblocks_it = 0
for g in range(nysteps):
	reg_nyblocks_jump = reg_nyblocks_it + yppc
	for h in range(nxsteps):
		reg_nxblocks_jump = reg_nxblocks_it + xppc
		if reg_nxblocks_it == 0 and reg_nyblocks_it == 0:
			cv2.rectangle(image,(reg_nxblocks_it, reg_nyblocks_it),(reg_nxblocks_jump, reg_nyblocks_jump),(0,255,0),3)
		elif reg_nxblocks_it == 0 and reg_nyblocks_it != 0:
			cv2.rectangle(image,(reg_nxblocks_it, reg_nyblocks_it // 2),(reg_nxblocks_jump, reg_nyblocks_jump // 2),(0,255,0),3)
		elif reg_nxblocks_it != 0 and reg_nyblocks_it == 0:
			cv2.rectangle(image,(reg_nxblocks_it // 2, reg_nyblocks_it),(reg_nxblocks_jump // 2, reg_nyblocks_jump),(0,255,0),3)
		else:
			cv2.rectangle(image,(reg_nxblocks_it // 2, reg_nyblocks_it // 2),(reg_nxblocks_jump // 2, reg_nyblocks_jump // 2),(0,255,0),3)
		reg_nxblocks_it = reg_nxblocks_it + xppc
		cv2.imshow('image', image)
		cv2.waitKey(1000)
		# time.sleep(2000)
		cv2.destroyAllWindows()
	reg_nxblocks_it = 0
	reg_nyblocks_it = reg_nyblocks_it + yppc

# plt.imshow(image)
# plt.show()

# cv2.imshow('image', image)
# k = cv2.waitKey(0)
# if k == 27:
# 	cv2.destroyAllWindows()