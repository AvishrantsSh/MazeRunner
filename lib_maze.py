import cv2
import numpy as np

class solver(object):
    
    sol_clr = [255,0,0]
    clr = [0,255]
    mazeinf = [0,0,0,0,50,0]
    arr = []
    res = []
    state = False
    
    def __init__(self,img):
        self.img = img
        self.dim = img.shape
<<<<<<< HEAD
        
=======
        self.sol_clr = [255,0,0]
        self.clr = [0,255]
        self.mazeinf = [0,0,0,0,50,0]
        self.arr = []
        self.res = []
        self.state = False

>>>>>>> 89208f1ac06ebcf1c91a54602bd764bf55d1f92d
    def getparam(self):
        ##This Function Needs Some serious shit of work            
        print("> Normalised")
        self.getbounds()
        self.rect_size()

    def getbounds(self):
        for x in range(0,self.dim[0]):
            st = True
            for y in range(0,self.dim[1]):
                if np.all(self.img[x][y] == 0):
                    solver.mazeinf[0] = y
                    solver.mazeinf[2] = x
                    st = False
                    break
            if st == False:
                break

        for x in range(self.dim[0],0,-1):
            st = True
            for y in range(self.dim[1],0,-1):
                if np.all(self.img[x-1][y-1] == 0):
                    solver.mazeinf[1] = y
                    solver.mazeinf[3] = x
                    st = False
                    break
            if st == False:
                break
        print("> Got Boundaries")

    def rect_size(self):
        index = 0
        for y in range(solver.mazeinf[0],solver.mazeinf[1]):
            x = solver.mazeinf[2]
            if np.all(self.img[x][y] == 255):
                if solver.mazeinf[5] == 0:
                    index = y
                solver.mazeinf[5] += 1

        counth = 0
        for x in range(solver.mazeinf[2],solver.mazeinf[3]):
            if np.all(self.img[x][index-1] == 0):
                counth += 1
            else:
                if solver.mazeinf[4] > counth and counth != 0:
                    solver.mazeinf[4] = counth
                counth = 0
        
        print("> Got Maze Struct. Info")

    def binarray(self):
        xt = 0
        yt = 0
        x = solver.mazeinf[0]
        while x < solver.mazeinf[1]:
            tmp=[]
            y = solver.mazeinf[2]         
            while y < solver.mazeinf[3]:
                if np.all(self.img[x][y] == 0):
                    tmp.append(0)
                else:
                    tmp.append(1)
            
                y += (solver.mazeinf[4] if yt % 2 == 0 else solver.mazeinf[5])
                yt += 1
            
            x += (solver.mazeinf[4] if xt % 2 == 0 else solver.mazeinf[5])
            xt += 1
            solver.arr.append(tmp) 

        coord = solver.arr[0].index(1)
        solver.res.append([0,coord])
        print("> Constructed Array")
        self.getsolindex(0,coord,0,0)

    def getsolindex(self,row,col,prow,pcol):
        if row == len(solver.arr) -  1:
            solver.state = True
            print("> Solution Found")
            return
        
        try:
                
            if solver.arr[row+1][col] == 1 and (prow != row+1 or pcol != col) and solver.state == False:
                solver.res.append([row+1,col])
                self.getsolindex(row+1,col,row,col)
            
            if solver.arr[row][col-1] == 1 and (prow != row or pcol != col-1) and solver.state == False:
                solver.res.append([row,col-1])
                self.getsolindex(row,col-1,row,col)
                        
            if solver.arr[row][col+1] == 1 and (prow != row or pcol != col+1) and solver.state == False:
                solver.res.append([row,col+1])
                self.getsolindex(row,col+1,row,col)
            
            if solver.arr[row-1][col] == 1 and (prow != row-1 or pcol != col) and solver.state == False:
                solver.res.append([row-1,col])
                self.getsolindex(row-1,col,row,col)
                
            if solver.state == False:
                solver.res = solver.res[:-1]
        except:
            print("Oops...No Solution Found")

    def construct(self):
        self.binarray()
        print("> Constructing...")
        self.img = cv2.cvtColor(self.img,cv2.COLOR_GRAY2RGB)
        x = solver.mazeinf[0]
        xt = 0
        while x < solver.mazeinf[1]:
            y = solver.mazeinf[2]
            yt = 0
            while y < solver.mazeinf[3]:
                if [xt,yt] in solver.res:
                    h,k = 0,0
                    k = solver.mazeinf[4] + y if yt % 2 == 0 else solver.mazeinf[5] + y
                    h = solver.mazeinf[4] + x if xt % 2 == 0 else solver.mazeinf[5] + x
                
                    self.img[x:h,y:k] = solver.sol_clr    
                
                y += (solver.mazeinf[4] if yt % 2 == 0 else solver.mazeinf[5])
                yt += 1
            
            x += (solver.mazeinf[4] if xt % 2 == 0 else solver.mazeinf[5])
            xt += 1
        
        print("Showing Result.")
        return self.img

    def details(self):
        print("Under Dev.")