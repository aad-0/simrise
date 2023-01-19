
import csv
import os

PATH = "B:\somestuff\simrise\\blalba\\new_tool\\images\\"
PATHPOOL = "B:\\somestuff\\simrise\\blalba\\new_tool\\images\\pool_new"
os.chdir(PATH)
fc = open("out.csv","r")
lc = fc.readlines()

imgs = [x.split(',')[0] for x in lc]
FILES = next(os.walk(PATHPOOL),(None,None,[]))[2]

_notin =[x for x in FILES if x not in imgs] 
#out = open("out_last.csv","w")
#outCursor = csv.writer(out, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
#
#new = []
#for i in _notin:
#    new.append(i +","+[a for a in lc if i in a][0][-6:-1])
#
#for i in new:
#    outCursor.writerow([i])
#
#
fc.close()


