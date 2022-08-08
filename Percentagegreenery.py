import cv2
import numpy as np
import os
from PIL import Image


os.chdir("/Users/Ada/Pictures/Vegitation" )

img = cv2.imread("image2.png")

Vegitation = np.array([35, 142, 106], np.uint8)
Vegitation1 = np.array([35, 142, 109], np.uint8)
dst = cv2.inRange(img, Vegitation, Vegitation1)
no_veg = cv2.countNonZero(dst)

Terrain = np.array([152,251,151], np.uint8)
Terrain1 = np.array([152,251,153], np.uint8)
dst1 = cv2.inRange(img, Terrain, Terrain1)
no_terrain = cv2.countNonZero(dst1)


Ground= np.array([81,  0, 79], np.uint8)
Ground1= np.array([81,  0, 82], np.uint8)
dst2 = cv2.inRange(img, Ground, Ground1)
no_ground = cv2.countNonZero(dst2)
print(no_ground)

Road = np.array([128, 64,127], np.uint8)
Road1 = np.array([128, 64,129], np.uint8)
dst3 = cv2.inRange(img, Road, Road1)
no_road = cv2.countNonZero(dst3)
print(no_road)

Sidewalk = np.array([232, 35,243], np.uint8) 
Sidewalk1 = np.array([232, 35,123], np.uint8) 
dst4 = cv2.inRange(img, Sidewalk, Sidewalk1)
no_sidewalk = cv2.countNonZero(dst4)


print('The number of vegitation pixels is: ' + str(no_veg))

Val= no_veg/ (no_veg +no_terrain+ no_ground + no_road+ no_sidewalk )


print("The percentage of total potentially greenery is: " + str(Val))

# this is the changes