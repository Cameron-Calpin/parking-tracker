# Classifier demonstration on different videos:
from imutils.object_detection import non_max_suppression
import cv2
import numpy as np

def perform_classification(video_src, cascade_src):
    cap = cv2.VideoCapture(video_src)
    car_cascade = cv2.CascadeClassifier(cascade_src)
    while True:
        ret, img = cap.read()
        if (type(img) == type(None)):
            print('Video not found')
            break
        image_scaled = cv2.resize(img, None, fx=1.0, fy=1.0)
        gray = cv2.cvtColor(image_scaled, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.2, 1) #1.1, 1
                                                        # 7 , 1
        cars = np.array([[x, y, x + w, y + h] for (x, y, w, h) in cars])
        pick = non_max_suppression(cars, probs=None, overlapThresh=0.65)
        for (x, y, w, h) in pick:
            # cv2.rectangle(image_scaled, (x, y), (x + w, y + h), (0 , 255, 255), 2) #bgr
            cv2.rectangle(image_scaled, (x, y), (w,  h), (0, 255, 255), 2)
        cv2.imshow('Press ESC key to finish', image_scaled)

            # press escape key to exit
        if cv2.waitKey(33) == 27:
            break
    print('Execution finished')
    cv2.destroyAllWindows()

perform_classification('parking_garage_2.mp4', 'Khare_training_01/data/cascade.xml')
perform_classification('parking_garage_2.mp4', 'Khare_training_01/data_2/cascade.xml')
# perform_classification(0, 'Khare_training_01/data_3/cascade.xml')
# perform_classification('parking_garage.mp4', 'Khare_classifier_01.xml')
# perform_classification('parking_garage.mp4', 'Khare_classifier_02.xml')    # press escape to finish
perform_classification('parking_garage_2.mp4', 'Khare_classifier_01.xml')
# perform_classification('parking_garage_2.mp4', 'Khare_classifier_02.xml')

# perform_classification('Khare_testvideo_01.mp4', 'Khare_classifier_01.xml')    # press escape to finish
# perform_classification('Khare_testvideo_01.mp4', 'Khare_classifier_02.xml')
# perform_classification('Khare_testvideo_02.avi', 'Khare_classifier_01.xml')    # M6 highway Britain
# perform_classification('Khare_testvideo_02.avi', 'Khare_classifier_02.xml')    # M6 highway Britain

