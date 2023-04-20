import cv2
import numpy as np

img = cv2.imread("solar-system.jpg")
cv2.putText(img, "Sun", (20,300), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5, (255,255,255))
cv2.putText(img, "Mercury", (120,240), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.65, (255,255,255))
cv2.putText(img, "Venus", (190,260), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.65, (255,255,255))
cv2.putText(img, "Earth", (290,270), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.65, (255,255,255))
cv2.putText(img, "Mars", (385,250), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.65, (255,255,255))
cv2.putText(img, "Jupiter", (570,380), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.65, (255,255,255))
cv2.putText(img, "Saturn", (770,280), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.65, (255,255,255))
cv2.putText(img, "Uranus", (970,280), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.65, (255,255,255))
cv2.putText(img, "Neptune", (1120,280), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.65, (255,255,255))
cv2.imshow("Display Image",img) 

cv2.waitKey(0)