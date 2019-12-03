# implements the HAAR classifier on the given video (Expected out from a properly trained classifier)
import cv2
# import msvcrt as m
import numpy as np
import imutils as im
from imutils.object_detection import non_max_suppression

# def wait():
#     m.getch()

def get_acc(cascade_src):
    # video_src = 'dataset/video2.avi'
    # Total = [157,156,156,154,156] #manually determined by counting
    Total = [12,12,12,12,12,12,12,12,12,12] # parking_garage_test
    # Total = [10,11,12,12,12,11,11,11,11,10] # parking_garage_2_test
    car_cascade = cv2.CascadeClassifier(cascade_src)
    counter = 1
    index =0
    list_of_indexes = []
    while True:
        # ret, img = cap.read()
        # if (type(img) == type(None)):
        #     break

        if counter<11:
            img_name = 'parking_garage_test_%d.png' % counter
            img_init = cv2.imread(img_name)
            img = cv2.resize(img_init, None, fx=0.6, fy=0.6)
        else:
            break
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ''' Change these parameters to gain the highest accuracy '''
        cars = car_cascade.detectMultiScale(gray, 1.818, 4) # 1.1, 1
                                                          # 1.2, 2  
        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in cars])
        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

        # draw the final bounding boxes
        for (xA, yA, xB, yB) in pick:
            cv2.rectangle(img, (xA, yA), (xB, yB), (0, 255, 0), 2)
        # for (x, y, w, h) in cars:
        #     cv2.rectangle(img, (x, y), (x + w, y + h), (0 , 0, 255), 2) #bgr
            index+=1
        # cv2.imshow('video2', img)
        # cv2.imshow('image', img)
        counter+=1
        k = cv2.waitKey(0) # 32
        saved = index
        print("%d vehicles found" %saved)
        list_of_indexes.append(saved/Total[counter-2])
        index = 0
        # input("press ")
        if k== 32:
            continue
        # press escape key to exit
        if cv2.waitKey(33) == 27:
            break
        # os.system("pause")
    sum =0
    for i in list_of_indexes:
        # print('percent: ', i)
        sum = sum+ i

    percentage = (sum/len(list_of_indexes))*100
    print("Accuracy: ", percentage)
    cv2.destroyAllWindows()
    return percentage