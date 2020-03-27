#Applicable Only for Rectangle-Cell Mazes

import cv2,sys,time
import numpy as np
#from termcolor import colored

sys.setrecursionlimit(10**6)
start = time.time()

#Change the indentation fo solution_path here
#sol_ind = 1

#[b,g,r] format
sol_clr = [255,0,0]
path = 255
border = 0
mh,mw = 50,0
sr,er,sc,ec = 0,0,0,0
arr = []
res = []
state = False
def normalise():
    global img,dim
    ##This Function Needs Some serious shit of work            
    print("Normalised")
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
    print("Got Boundaries")

def rect_size():
    global mw,mh,sc,sr,ec,er,img
    index = 0
    for y in range(sc,ec):
        x = sr
        if np.all(img[x][y] == 255):
            if mw == 0:
                index = y
            mw += 1
            
    counth = 0
    for x in range(sr,er):
        if np.all(img[x][index-1] == 0):
            counth += 1
        else:
            if mh > counth and counth != 0:
                mh = counth
            counth = 0
    
    print("Got Maze Info")

def binarray():
    global arr,img,dim
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
        
            y += (mh if yt % 2 == 0 else mw)
            yt += 1
        
        x += (mh if xt % 2 == 0 else mw)
        xt += 1
        arr.append(tmp) 

    coord = arr[0].index(1)
    res.append([0,coord])
    print("Constructed Array")
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
    print("Constructing")
    global sc,sr,ec,er,res,mh,mw,img,sol_ind
    img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
    x = sc
    xt = 0
    while x < ec:
        y = sr
        yt = 0
        while y < er:
            if [xt,yt] in res:
                h,k = 0,0
                k = mh + y if yt % 2 == 0 else mw + y
                h = mh + x if xt % 2 == 0 else mw + x
               
                img[x:h,y:k] = sol_clr    
            
            y += (mh if yt % 2 == 0 else mw)
            yt += 1
        
        x += (mh if xt % 2 == 0 else mw)
        xt += 1
    ##This Part is Under Development and might not work perfectly..Result won't be affected if uncommented
    
    # for h in range(sc,ec):
    #     for k in range(sr,er):
    #         if np.all(img[h][k] == 0):
    #             try:
    #                 if np.all(img[h-sol_ind][k] == sol_clr):
    #                     img[h-sol_ind][k] = path

    #                 if np.all(img[h+sol_ind][k] == sol_clr):
    #                     img[h+sol_ind][k] = path

    #                 if np.all(img[h][k-sol_ind] == sol_clr):
    #                     img[h][k-sol_ind] = path

    #                 if np.all(img[h][k+sol_ind] == sol_clr):
    #                     img[h][k+sol_ind] = path
                        
    #             except:
    #                 logging.error("401: Index Out of Bounds")
    print("Showing Resultant")

#adjust location as per your convenience
origimg = cv2.imread("/home/avishrant/GitRepo/MazeRunner/Maze/maze8.png")
(thresh, img) = cv2.threshold(cv2.cvtColor(origimg, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)

dim = img.shape
print("Under Development")

print("The process may take time, according to complexity and size of maze")
normalise()
construct()

##Uncomment to see Image Details
#print("Minimum Edge :",mh,"\n","Minimum Path :",mw,"\n","Starting Col :",sc,"\n","Starting Row :",sr,"\n","Ending Col :",ec,"\n","Ending Row :",er,sep='')
##Uncomment to see the binary-array
# for x in arr:
#     print(*x , sep = ' ')

end = time.time()
print("Execution Time :",end-start,"s")
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
