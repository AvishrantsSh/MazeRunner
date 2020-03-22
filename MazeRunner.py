#Applicable Only for Square-Cell Mazes                                                                         Mazes

import cv2
import numpy as np

mh , mw = 100 , 100
def normalise(img, dim):
    for x in range(0,dim[0]):
        for y in range(0,dim[1]):
            if np.any(img[x][y] != 255):
                img[x][y] = [0,0,0]
    sarr(img,dim)

def getmin(img , dim):
    global mw,mh

    for x in range(0,dim[0]):
        countw = 0
        st = True
        snum = 0
        enum = 0
        for y in range(0,dim[1]):
            if np.all(img[x][y] == 0):
                snum = y
                break

        for y in range(dim[1],0,-1):
            if np.all(img[x][y-1] == 0):
                enum = y
                break
        

        for y in range(snum,enum):
            if np.all(img[x][y] == 255):
                img[x][y] = [255,255,0]
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

    for y in range(0,dim[1]):
        counth = 0
        st = True
        snum = 0
        enum = 0
        for x in range(0,dim[0]):
            if np.all(img[x][y] == 255):
                snum = x
                break

        for x in range(dim[0],0,-1):
            if np.all(img[x-1][y] == 255):
                enum = x
                break

        for x in range(snum,dim[0]):
            if np.all(img[x][y] == 0):
                img[x][y] = [0,0,255]
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
    getmin(img,dim)
    print("Under Development")
    print(mh,mw)


#adjust location as per your convenience
img = cv2.imread("/home/avishrant/GitRepo/MazeRunner/maze.png")
#img = cv2.resize(oimg, (300,300), interpolation = cv2.INTER_AREA)
dim = img.shape
normalise(img,dim)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
