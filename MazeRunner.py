#Applicable Only for Rectangle-Cell Mazes

import cv2,sys
import numpy as np
#from termcolor import colored
sys.setrecursionlimit(10**6)


#[b,g,r] format
sol_clr = [255,0,0]
path = [255,255,255]
border = [0,0,0]

mh,mw = 100,100
sr,er,sc,ec = 0,0,0,0
arr = []
res = []
state = False
def normalise():
    global img,dim
    for x in range(0,dim[0]):
        for y in range(0,dim[1]):
            if np.any(img[x][y] != 255):
                img[x][y] = border
    getbounds()
    rect_size()

def getbounds():
    global sc,sr,ec,er,img,dim
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

def rect_size():
    global mw,mh,sc,sr,ec,er,img

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

def binarray():
    # print(mh,mw)
    # print(sc,ec,sr,er)
    global arr,img,dim
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
    getsolindex(0,coord,0,0)

def getsolindex(row,col,prow,pcol):
    global res,arr,state
    if row == len(arr) -  1:
        state = True
        print("Solution Found")
        return
    

    try:
            
        if arr[row+1][col] == 1 and (prow != row+1 or pcol != col) and state == False:
            res.append([row+1,col])
            getsolindex(row+1,col,row,col)
        
        if arr[row][col-1] == 1 and (prow != row or pcol != col-1) and state == False:
            res.append([row,col-1])
            getsolindex(row,col-1,row,col)
                    
        if arr[row][col+1] == 1 and (prow != row or pcol != col+1) and state == False:
            res.append([row,col+1])
            getsolindex(row,col+1,row,col)
        
        if arr[row-1][col] == 1 and (prow != row-1 or pcol != col) and state == False:
            res.append([row-1,col])
            getsolindex(row-1,col,row,col)
            
        if state == False:
            res = res[:-1]
        
    except:
        print("Oops...No Solution Found")

def construct():
    binarray()
    global sc,sr,ec,er,res,mh,mw,img
    x = sc
    xt = 0
    while x < ec:
        y = sr
        yt = 0
        while y < er:
            if [xt,yt] in res:
                h,k = 0,0
                if yt % 2 == 1:
                    k = mw

                else:
                    k = mh

                if xt % 2 == 1: 
                    h = mw

                else:
                    h = mh
                
                h += x
                k += y
                img[x:h,y:k] = sol_clr    

            if yt % 2 == 1:
                y += mw

            else:
                y += mh    
            yt += 1
        
        if xt % 2 == 1:
            x += mw
        else:
            x += mh
        
        xt += 1

    for h in range(sc,ec):
        for k in range(sr,er):
            if np.all(img[h][k] == 0):
                try:
                    if np.all(img[h-1][k] == sol_clr):
                        img[h-1][k] = path

                    if np.all(img[h+1][k] == sol_clr):
                        img[h+1][k] = path

                    if np.all(img[h][k-1] == sol_clr):
                        img[h][k-1] = path

                    if np.all(img[h][k+1] == sol_clr):
                        img[h][k+1] = path
                        
                except:
                    print("Error 401:Ignoring")
    print("Showing Resultant")

#adjust location as per your convenience
img = cv2.imread("/home/avishrant/GitRepo/MazeRunner/Maze/maze8.png")
dim = img.shape
print("Under Development")

print("The process may take time, according to complexity and size of maze")
normalise()
construct()

cv2.imshow("Image", img)
#cv2.imshow("Image" , resimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
