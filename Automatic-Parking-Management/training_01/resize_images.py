from PIL import Image
import os
import sys
import glob
import matplotlib.image as mpimg
import cv2

directory = '/home/frostbyte/Desktop/CNU/parking-tracker/Automatic-Parking-Management/Khare_training_01/negative'
out_directory = '/home/frostbyte/Desktop/CNU/parking-tracker/Automatic-Parking-Management/Khare_training_01/negative_resize'

# for file_name in os.listdir(directory):
#   print("Processing %s" % file_name)
#   image = Image.open(os.path.join(directory, file_name))

#   output = image.resize((128, 64), Image.ANTIALIAS)

#   output_file_name = os.path.join(directory, file_name)
#   output.save(output_file_name, "JPEG", quality = 95)

# print("All done")


'''
Debugging array dimensions for HSV (Should be 3 dimensions)
'''
# count = 0;
# for f in glob.glob('/home/frostbyte/Desktop/CNU/parking-tracker/Automatic-Parking-Management/Khare_training_01/negative_resize/*.jpg'):
# 	img = mpimg.imread(f)
# 	if img.shape != (64, 128, 3):
# 		im = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
# 		print(f, img.shape)
# 		print(f, im.shape)
# 		cv2.imwrite('/home/frostbyte/Desktop/CNU/parking-tracker/Automatic-Parking-Management/Khare_training_01/negative_resize_colorconverted/' + str(count) + '.jpg', im)
# 	else:
# 		cv2.imwrite('/home/frostbyte/Desktop/CNU/parking-tracker/Automatic-Parking-Management/Khare_training_01/negative_resize_colorconverted/' + str(count) + '.jpg', img)
# 	count += 1

for f in glob.glob('/home/frostbyte/Desktop/CNU/parking-tracker/Automatic-Parking-Management/Khare_training_01/negative_resize_colorconverted/*.jpg'):
	img = mpimg.imread(f)
	if img.shape != (64, 128, 3):
		print(f, img.shape)
	print(f, img.shape)
