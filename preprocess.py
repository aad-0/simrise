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

PATH = f"B:\\somestuff\\simrise\\blalba\\new_tool\\images\\"
PATHIN = f"B:\\somestuff\\simrise\\blalba\\new_tool\\images\\{sys.argv[1]}\\"
PATHOUT = f"B:\\somestuff\\simrise\\blalba\\new_tool\\images\\{sys.argv[2]}\\"
os.chdir(PATH);
FILES = next(os.walk(PATHIN),(None,None,[]))[2];



for file in FILES:
    img = cv.imread(f"{PATHIN}\\{file}\\");
    red =   img[:,:,0]
    green = img[:,:,1]
    #blue=   img[:,:,2]
    #print("RED",red,"\nGREEN",green,"\nBLUE",blue);
    #cv.imshow("origin",img)
    img_rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB);
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    hsvgrb = cv.cvtColor(img_rgb,cv.COLOR_BGR2HSV)
    hsvrgb = cv.cvtColor(img_rgb,cv.COLOR_BGR2HSV)
    
    #cv.imwrite(f"{PATHOUT}\\red_{file}",red)
    #cv.imwrite(f"{PATHOUT}\\green_{file}",green)
    #cv.imwrite(f"{PATHOUT}\\blue_{file}",blue)
    #cv.imwrite(f"{PATHOUT}\\hsvgrb_{file}",hsvgrb)

    cv.imwrite(f"{PATHOUT}\\rgbX_{file}",img)    
    cv.imwrite(f"{PATHOUT}\\rgb1_{file}",img)    
    #cv.imwrite(f"{PATHOUT}\\gray_{file}",gray)
    #cv.imwrite(f"{PATHOUT}\\hsvrgb_{file}",hsvrgb)
    
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


