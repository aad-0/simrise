#/usr/bin/python

import cv2 as cv
import numpy as np

class GetCorner(object): 
    def __init__(self,img,count = 4):
        self.count = count;
        self.img = img;#cv.imread(fname,1);
        self.page = "page";
        self.points = list();

        cv.imshow(self.page,self.img);
        cv.setMouseCallback(self.page, self.click_event);
        cv.waitKey(0);
        #cv.destroyAllWindows();

    def click_event(self,event,x,y,flags,params):
        if(self.count <= 0):
            return;
        if (event == cv.EVENT_LBUTTONDOWN):
            print("LOG",x,y);
            cv.circle(self.img,(x,y),5,(255,255,255),cv.FILLED);
            cv.putText(self.img,f"{x},{y}", (x,y),cv.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1);
            cv.imshow(self.page,self.img);
            self.points.append((x,y));
            self.count -= 1;

    def clearPoints(self):
        self.points.clear();
    def getPoints(self):
        return self.points.copy();

    def getCropped(self):
        #self.points.sort();
        A = self.points[0];
        B = self.points[1];
        C = self.points[2];
        D = self.points[3];
        widthAD = np.sqrt(((A[0] - D[0]) **2) + ((A[1] - D[1]) **2));
        widthBC = np.sqrt(((B[0] - C[0]) **2) + ((B[1] - C[1]) **2));
        MAXW = max(int(widthAD), int(widthBC));


        heightAB = np.sqrt(((A[0] - B[0]) **2) + ((A[1] - B[1]) **2));
        heightCD = np.sqrt(((C[0] - D[0]) **2) + ((C[1] - D[1]) **2));
        MAXH = max(int(heightAB),int(heightCD));

        matrixOut = np.float32([[0,0],[0,MAXH -1],[MAXW -1, MAXH -1],[MAXW -1,0]])

        pt = cv.getPerspectiveTransform(np.float32(self.points),matrixOut);
        out = cv.warpPerspective(self.img,pt,(MAXW,MAXH),flags=cv.INTER_LINEAR)
        return out

FILE = "B:\\somestuff\simrise\\blalba\\new_tool\\images_all\\IMGT0070.PNG"

img = cv.imread(FILE,1);
#cv.imshow('file',img);
#cv.setMouseCallback('file',GetCorner.click_event);
#
#cv.waitKey(0);
c = GetCorner(img);
a = c.getCropped();
cv.imshow('a',a);
cv.waitKey(0);
cv.destroyAllWindows();



