import cv2
import numpy as np

cap = cv2.VideoCapture("parking_garage_2.mp4")
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1000)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)


while(1):
	# Take each frame
	_, frame = cap.read()
	frame = cv2.resize(frame, None, fx=0.4, fy=0.4)

	# Apply Guassian Filter to blur image and reduce noise
	frame_blur = cv2.GaussianBlur(frame, (5,5), 3)

	# Convert BGR to GRAY
	frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	

	cv2.imshow('original', frame)
	cv2.imshow('gray', frame_gray)
	cv2.imshow('guassian', frame_blur)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
