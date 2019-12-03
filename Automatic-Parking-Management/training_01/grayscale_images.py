import glob
import shutil
import cv2
import numpy as np
import os

def store_raw_images():
	src_dir = '/home/frostbyte/Desktop/CNU/parking-tracker/Automatic-Parking-Management/Khare_training_01/negative/'
	files = [f for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))]

	pic_num = 0
    
	if not os.path.exists('/home/frostbyte/Desktop/CNU/parking-tracker/Automatic-Parking-Management/Khare_training_01/neg'):
		os.makedirs('/home/frostbyte/Desktop/CNU/parking-tracker/Automatic-Parking-Management/Khare_training_01/neg')

	dst_dir = '/home/frostbyte/Desktop/CNU/parking-tracker/Automatic-Parking-Management/Khare_training_01/neg/'
        
	for i in files:
		try:
			print(i)
			img = cv2.imread(src_dir + i, cv2.IMREAD_GRAYSCALE)
			# should be larger than samples / pos pic (so we can place our image on it)
			resized_image = cv2.resize(img, (100, 100))
			cv2.imwrite(dst_dir + str(pic_num) + ".jpg", resized_image)
			pic_num += 1
            
		except Exception as e:
			print(str(e))

def create_bg():
	dst_dir = '/home/frostbyte/Desktop/CNU/parking-tracker/Automatic-Parking-Management/Khare_training_01/neg/'
	files = [f for f in os.listdir(dst_dir) if os.path.isfile(os.path.join(dst_dir, f))]
	for f in files:
		line = dst_dir + f + '\n'
		with open('/home/frostbyte/Desktop/CNU/parking-tracker/Automatic-Parking-Management/Khare_training_01/bg.txt','a') as f:
			f.write(line)


if __name__ == "__main__":
#	store_raw_images()
	create_bg()
