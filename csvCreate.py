import csv
import cv2 as cv
import sys
import os

LABELS = ["Id","Bypass Diode","Junction Box","MHotspot","SHotspot"]; #,""]

PATH = "B:\\somestuff\\simrise\\blalba\\new_tool\\images\\"
FILELABELS = ["Bypass Diode-crop","Junction box-crop","Multi cell hotspot-crop","Single cell hotspot-crop"]
#not in use
#PATHOUT = "B:\\somestuff\\simrise\\blalba\\new_tool\\images\\pool_gray\\"
FILECROP = sys.argv[1]; # raw_pool
OUT = sys.argv[2]; # *.csv
os.chdir(PATH)

FILES = next(os.walk(FILECROP),(None,None,[]))[2];
#FILES = [x for x in FILES if x.startswith("origin_")]

print(FILES)
print("LEN FILES", len(FILES))
#FILETAGS = ["origin_","red_","green_","gray_","hsvgrb_","hsvrgb_"]
FILETAGS = ["rgb_","gray_","hsvrgb_"]


out = open(OUT,"a")
outCursor = csv.writer(out, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
if(input("First ?: ") == '1'):
    outCursor.writerow(LABELS)

l = len(FILES);
i = 0;
while(i < l ):
    print(f"{FILECROP}\\{FILES[i]}\\ i:l",i,l)
    #img = cv.imread(f"{PATH}\\{FILECROP}\\{FILES[i]}\\")
    #cv.imshow("IMG",img)
    #cv.waitKey(1);
    flag = True;
    tags = [0,0,0,0];
    while(flag or len(tags) != len(LABELS) -1 and i < 4):
        print("FLAG",flag,"LENTAG",len(tags))
        k = 0
        print(f"FILE {FILES[i][FILES[i].find('_')+1:]}")
        for d in FILELABELS:
            if(os.path.exists(f"{PATH}\\{d}\\{FILES[i][FILES[i].find('_')+1:]}")):
                print("labeled: ",d, end=" ")
                tags[k] = 1
            k+=1;
        print("")
        print(dict(zip(LABELS[1:],tags)));
        #tags = [x for x in input("TAGS: ")]
        
        try:
            flag = False;
            #flag = not int(input("Done? 1/0: "));
        except:
            print("??")
            flag = True
            continue;

    #cv.destroyAllWindows();

    #for ftag in FILETAGS:
    #    t = tags.copy()
    #    t.insert(0,f"{ftag}{FILES[i][7:]}")
    #    print("WRITE TAGS",t)
    #    outCursor.writerow(t)
    t  = tags.copy()
    t.insert(0,f"{FILES[i]}")
    print("WRITE TAGS", t)
    outCursor.writerow(t)

    i += 1

out.close()

