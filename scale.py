import cv2 as cv
import os
import sys

PATHIN =    sys.argv[1]#"B:\\somestuff\\simrise\\blalba\\new_tool\\images\\pool\\"
PATHOUT =   sys.argv[2]#"B:\\somestuff\\simrise\\blalba\\new_tool\\images\\pool_new\\"
PATH =      "B:\\somestuff\\simrise\\blalba\\new_tool\\images\\"

os.chdir(PATH)

SIZE = 200
FILES = next(os.walk(PATHIN),(None,None,[]))[2];

l = len(FILES)
i = 0
while(i < l):
    imgin = cv.imread(f"{PATHIN}\\{FILES[i]}")
    #imgin = imgin / 255.0
    imgout = cv.resize(imgin, (SIZE,SIZE), interpolation = cv.INTER_LINEAR)

    cv.imwrite(f"{PATHOUT}\\{FILES[i]}",imgout)

    i += 1;






