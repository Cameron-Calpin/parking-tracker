import cv2
import sys

# Gets the name of the image file (filename) from sys.argv

imagePath = sys.argv[1]
cascPath = "Khare_training_01/data_2/cascade.xml"
#cascPath = "Khare_classifier_02.xml"
# This creates the cascade classifcation from file 

carCascade = cv2.CascadeClassifier(cascPath)

# The image is read and converted to grayscale

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# The face or faces in an image are detected
# This section requires the most adjustments to get accuracy on face being detected.


cars = carCascade.detectMultiScale(gray, 3.5, 2)

print("Detected {0} cars!".format(len(cars)))

# This draws a green rectangle around the faces detected


for (x, y, w, h) in cars:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Cars Detected", image)

#k = cv2.waitKey(30) & 0xFF
#if k == 27: # wait for ESC key to exit
#	cv2.destroyAllWindows()
print('Execution finished')
cv2.waitKey(0)
