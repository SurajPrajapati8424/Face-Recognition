import numpy as np
import cv2

import time
import urllib
import requests
__URL = 'http://192.168.0.10:35355/'

print("Hello World")

# cap = cv2.VideoCapture(0)
# ret, frame = cap.read()

# while(True):
#     ret, frame = cap.read()

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     cv2.imshow('frame',gray)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
cam = cv2.VideoCapture(__URL)
check, img = cam.read()
while True:
    check, img = cam.read()
    cv2.imshow('IPWebcam', img)
    height, width, channels = img.shape
    print(height, width, channels)
    if cv2.waitKey(1) == 27:
      break

cam.release()
cv2.destroyAllWindows()