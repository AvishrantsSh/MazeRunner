#Applicable Only for Square-Cell Mazes

import cv2
import numpy as np
mh,mw = 100,100
sr,er,sc,ec = 0,0,0,0

def normalise(img, dim):
    for x in range(0,dim[0]):
        for y in range(0,dim[1]):
            if np.any(img[x][y] != 255):
                img[x][y] = [0,0,0]
    sarr(img,dim)

def getstart(img,dim):
    global sc,sr,ec,er

    for x in range(0,dim[0]):
        st = True
        for y in range(0,dim[1]):
            if np.all(img[x][y] == 0):
                sc = y
                sr = x
                st = False
                break
        if st == False:
            break

    for x in range(dim[0],0,-1):
        st = True
        for y in range(dim[1],0,-1):
            if np.all(img[x-1][y-1] == 0):
                ec = y
                er = x
                st = False
                break
        if st == False:
            break

def getmin(img):
    global mw,mh,sc,sr,ec,er

    for x in range(sc,ec):
        countw = 0
        st = True
        
        for y in range(sr,er):
            if np.all(img[x][y] == 255):
                countw += 1
                st = False

            else:
                if st == False and y == dim[1] - 1:
                    break
                else:
                    if mw > countw and countw != 0:
                        mw = countw
                    countw = 0
                
             
        if mw > countw and countw != 0:
            mw = countw

    for y in range(sr,er):
        counth = 0
        st = True
        
        for x in range(sc,ec):
            if np.all(img[x][y] == 0):
                counth += 1
                st = False

            else:
                if st == False and x == dim[0] - 1:
                    break
                else:
                    if mh > counth and counth != 0:
                        mh = counth
                    counth = 0

        if mh > counth and counth != 0:
            mh = counth

def sarr(img, dim):
    getstart(img,dim)
    getmin(img)
    print("Under Development")
    print(mh,mw)
    

#adjust location as per your convenience
img = cv2.imread("/home/avishrant/GitRepo/MazeRunner/maze.png")
dim = img.shape
normalise(img,dim)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
