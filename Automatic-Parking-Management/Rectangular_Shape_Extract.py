# Python program to extract rectangular 
# Shape using OpenCV in Python3 
import cv2 
import numpy as np  

cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1000)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Background Subtraction
    frame_blur = cv2.GaussianBlur(frame.copy(), (5,5), 3)
    # frame_blur = frame_blur[150:1000, 100:1800]
    frame_gray = cv2.cvtColor(frame_blur, cv2.COLOR_BGR2GRAY)
    frame_out = frame.copy()

    kernel_erode = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3)) # morphological kernel
    kernel_dilate = cv2.getStructuringElement(cv2.MORPH_RECT,(5,19))

    # hog = cv2.HOGDescriptor()
    # hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    fgbg = cv2.createBackgroundSubtractorMOG2(history=300, varThreshold=16, detectShadows=True)
    # frame_blur = frame_blur[380:420, 240:470]
    # cv2.imshow('dss', frame_blur)
    fgmask = fgbg.apply(frame_blur)
    bw = np.uint8(fgmask==255)*255
    bw = cv2.erode(bw, kernel_erode, iterations=1)
    bw = cv2.dilate(bw, kernel_dilate, iterations=1)
    # cv2.imshow('dss',bw)
    # cv2.imwrite("frame%d.jpg" % co, bw)
    (_, cnts, _) = cv2.findContours(bw.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # loop over the contours
    for c in cnts:
        # print(cv2.contourArea(c))
        # if the contour is too small, we ignore it
        if cv2.contourArea(c) < 500:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame_out, (x, y), (x + w, y + h), (255, 0, 0), 1)

    # # detect people in the image. Slows down the program, requires high GPU speed
    # (rects, weights) = hog.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.05)
    # # draw the  bounding boxes
    # for (x, y, w, h) in rects:
    #     cv2.rectangle(frame_out, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Draw rectancle on screen
    cv2.rectangle(frame,(900,450),(500,200),(0,255,0),6)

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()