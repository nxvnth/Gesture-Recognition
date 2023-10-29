import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
from PIL import Image
import math
#<--------------------------------------------------------------------------------------------------------->
cap = cv2.VideoCapture(0) # 0 -> id no.of the webcam
detector = HandDetector(maxHands=2)

offset = 20
imgSize = 300

# <--------------------------------------------------------------------------------------------------------->
#Saving Image module
folder = "Data\A"



# <--------------------------------------------------------------------------------------------------------->
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    
    if hands:
        hand = hands[0]
        x,y,w,h = hand['bbox']
        
        imgWhite = np.ones((imgSize,imgSize,3),np.uint8)*255 
        
        imgCrop = img[y-offset:y+h+offset, x-offset:x+w+offset]
        # print(y-offset)
        # print(y+h+offset)
        # print(x-offset)
        # print(x+w+offset)
        
        # Process of image overlay
        #  imgCrop is superimposed on imgWhite
        
        imgCropShape = imgCrop.shape
        # print(imgCropShape)
        aspectRatio_h = h/w
        aspectRatio_w = w/h
        
        if aspectRatio_h > 1:
            k = imgSize/h
            wCal = math.ceil(k*w)
            
            wGap = math.ceil((imgSize-wCal)/2)
            
            imgResize = cv2.resize(imgCrop, (wCal,imgSize))
            imgResizeShape = imgResize.shape
        
            imgWhite[0:imgResizeShape[0], wGap:wCal+wGap] = imgResize
            
        if aspectRatio_w > 1:
            k = imgSize/w
            hCal = math.ceil(k*h)
            
            hGap = math.ceil((imgSize-hCal)/2)
            
            imgResize = cv2.resize(imgCrop, (imgSize,hCal))
            imgResizeShape = imgResize.shape
        
            imgWhite[hGap:hGap+hCal, 0:imgResizeShape[1]] = imgResize
        
        
        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# <--------------------------------------------------------------------------------------------------------->
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)
