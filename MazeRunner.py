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
    for x in range(1,dim[0] - 1):
        countw = 0
        st = True
        for y in range(1,dim[1] - 1):
            if np.all(img[x][y] == 255):
                countw += 1
                st = False
            else:
                if st == False:
                    break
        if mw > countw and countw != 0:
            mw = countw

    for y in range(1,dim[1] - 1):
        counth = 0
        st = True
        for x in range(1,dim[0] - 1):
            if np.all(img[x][y] == 0):
                counth += 1
                st = False
            else:
                if st == False:
                    break

        if mh > counth and counth != 0:
            mh = counth

def sarr(img, dim):
    getmin(img,dim)
    print("Under Development")
    print(mh,mw)


#adjust location as per your convenience
img = cv2.imread("/home/avishrant/GitRepo/MazeRunner/maze.png")
dim = img.shape
normalise(img,dim)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
