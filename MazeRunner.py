#Applicable Only for Rectangle-Cell Mazes

import cv2
import numpy as np
from termcolor import colored

mh,mw = 100,100
sr,er,sc,ec = 0,0,0,0
arr = []
res = []
state = False
def normalise(img, dim):
    for x in range(0,dim[0]):
        for y in range(0,dim[1]):
            if np.any(img[x][y] != 255):
                img[x][y] = [0,0,0]
    getmstart(img,dim)
    getsize(img)

def getmstart(img,dim):
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

def getsize(img):
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
    print("Under Development")
    print(mh,mw)
    print(sc,ec,sr,er)
    global arr
    #Tough Job Starts Here
    xt = 0
    yt = 0
    x = sc
    while x < ec:
        tmp=[]
        y = sr        
        while y < er:
            if np.all(img[x][y] == 0):
                tmp.append(0)
            else:
                tmp.append(1)
        
            if(yt % 2 == 1):
                y += mw
            else:
                y += mh
            yt += 1
        
        if(xt % 2 == 1):
            x += mw
        else:
            x += mh
        xt += 1
        arr.append(tmp) 

    coord = arr[0].index(1)
    res.append([0,coord])

    getsol(0,coord,0,0)

def getsol(row,col,prow,pcol):
    global res,arr,state
    if row == len(arr) -  1:
        state = True
        print("Reached")
        return
    

    try:    
        if arr[row][col-1] == 1 and (prow != row or pcol != col-1) and state == False:
            res.append([row,col-1])
            getsol(row,col-1,row,col)
                    
        if arr[row][col+1] == 1 and (prow != row or pcol != col+1) and state == False:
            res.append([row,col+1])
            getsol(row,col+1,row,col)
        
        if arr[row+1][col] == 1 and (prow != row+1 or pcol != col) and state == False:
            res.append([row+1,col])
            getsol(row+1,col,row,col)
        
        if arr[row-1][col] == 1 and (prow != row-1 or pcol != col) and state == False:
            res.append([row-1,col])
            getsol(row-1,col,row,col)
            
        if x == False:
            res = res[:-1]
        
    except:
        print("Oops")

        
#adjust location as per your convenience
img = cv2.imread("/home/avishrant/GitRepo/MazeRunner/Maze/maze3.png")
dim = img.shape
normalise(img,dim)
sarr(img,dim)

for x in range(0,len(arr)):
    for y in range(0,len(arr[0])):
        if [x,y] in res:
            print(colored(arr[x][y],'red'),end=' ')
        else:
            print(arr[x][y],end = ' ')
    print()    
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
