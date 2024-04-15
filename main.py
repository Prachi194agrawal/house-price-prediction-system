# This is a sample Python script.
import cv2
#import mediapipe as mp
import time
cap = cv2.VideoCapture(0)
#hands = mpHands.Hands()
while True:
    success, img = cap.read()
    imgRGB= cv2.cvtColor(img, cv2.COLORMAP_WINTER)
    cv2.imshow("Image", imgRGB)
    cv2.waitKey(1)