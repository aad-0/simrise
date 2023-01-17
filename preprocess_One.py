#/usr/bin/python

import cv2 as cv
import numpy as np
import sys
import os
#IMG = "B:\\somestuff\\simrise\\blalba\\new_tool\\images\\deneme\\IMGT0118.PNG\\"
#try:
#    IMG = sys.argv[1]
#    print("IMG",IMG)
#except:
#    sys.exit(-2)
#
PATHDENEME = "B:\\somestuff\\simrise\\blalba\\new_tool\\images\\deneme\\"

os.chdir(PATHDENEME);
FILES = next(os.walk(PATHDENEME),(None,None,[]))[2];

for f in FILES:
    img = cv.imread(f);
    red =   img[:,:,0]
    green = img[:,:,1]
    blue=   img[:,:,2]
    #print("RED",red,"\nGREEN",green,"\nBLUE",blue);
    #cv.imshow("origin",img)
    cv.imwrite(f"red_{f}",red)
    cv.imwrite(f"green_{f}",green)
    cv.imwrite(f"blue_{f}",blue)
    
    img_rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB);
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    hsvgrb = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    hsvrgb = cv.cvtColor(img_rgb,cv.COLOR_BGR2HSV)
    
    
    cv.imwrite(f"gray_{f}",gray)
    cv.imwrite(f"hsvgrb_{f}",hsvgrb)
    cv.imwrite(f"hsvrgb_{f}",hsvrgb)
    
#img = cv.imread(IMG);
#
#red =   img[:,:,0]
#green = img[:,:,1]
#blue=   img[:,:,2]
##print("RED",red,"\nGREEN",green,"\nBLUE",blue);
#cv.imshow("origin",img)
#cv.imshow("red",red)
#cv.imshow("green",green)
#cv.imshow("blue",blue)
#
#gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
#hsvFULL = cv.cvtColor(img,cv.COLOR_BGR2HSV_FULL)
#
#
#cv.imshow("gray",gray)
#cv.imshow("hsv",hsv)
#cv.imshow("hsvFULL",hsvFULL)
#
#
#

cv.waitKey(0);
cv.destroyAllWindows();


