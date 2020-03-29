import cv2
import numpy as np

class solver(object):
    def __init__(self,img):
        self.img = img
        self.dim = img.shape
        self.sol_clr = [255,0,0]
        self.clr = [0,255]
        self.mazeinf = [0,0,0,0,50,0]
        self.arr = []
        self.res = []
        self.state = False

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
                    self.mazeinf[0] = y
                    self.mazeinf[2] = x
                    st = False
                    break
            if st == False:
                break

        for x in range(self.dim[0],0,-1):
            st = True
            for y in range(self.dim[1],0,-1):
                if np.all(self.img[x-1][y-1] == 0):
                    self.mazeinf[1] = y
                    self.mazeinf[3] = x
                    st = False
                    break
            if st == False:
                break
        print("> Got Boundaries")

    def rect_size(self):
        index = 0
        for y in range(self.mazeinf[0],self.mazeinf[1]):
            x = self.mazeinf[2]
            if np.all(self.img[x][y] == 255):
                if self.mazeinf[5] == 0:
                    index = y
                self.mazeinf[5] += 1

        counth = 0
        for x in range(self.mazeinf[2],self.mazeinf[3]):
            if np.all(self.img[x][index-1] == 0):
                counth += 1
            else:
                if self.mazeinf[4] > counth and counth != 0:
                    self.mazeinf[4] = counth
                counth = 0
        
        print("> Got Maze Struct. Info")

    def binarray(self):
        xt = 0
        yt = 0
        x = self.mazeinf[0]
        while x < self.mazeinf[1]:
            tmp=[]
            y = self.mazeinf[2]         
            while y < self.mazeinf[3]:
                if np.all(self.img[x][y] == 0):
                    tmp.append(0)
                else:
                    tmp.append(1)
            
                y += (self.mazeinf[4] if yt % 2 == 0 else self.mazeinf[5])
                yt += 1
            
            x += (self.mazeinf[4] if xt % 2 == 0 else self.mazeinf[5])
            xt += 1
            self.arr.append(tmp) 

        coord = self.arr[0].index(1)
        self.res.append([0,coord])
        print("> Constructed Array")
        self.getsolindex(0,coord,0,0)

    def getsolindex(self,row,col,prow,pcol):
        if row == len(self.arr) -  1:
            self.state = True
            print("> Solution Found")
            return
        
        try:
                
            if self.arr[row+1][col] == 1 and (prow != row+1 or pcol != col) and self.state == False:
                self.res.append([row+1,col])
                self.getsolindex(row+1,col,row,col)
            
            if self.arr[row][col-1] == 1 and (prow != row or pcol != col-1) and self.state == False:
                self.res.append([row,col-1])
                self.getsolindex(row,col-1,row,col)
                        
            if self.arr[row][col+1] == 1 and (prow != row or pcol != col+1) and self.state == False:
                self.res.append([row,col+1])
                self.getsolindex(row,col+1,row,col)
            
            if self.arr[row-1][col] == 1 and (prow != row-1 or pcol != col) and self.state == False:
                self.res.append([row-1,col])
                self.getsolindex(row-1,col,row,col)
                
            if self.state == False:
                self.res = self.res[:-1]
        except:
            print("Oops...No Solution Found")

    def construct(self):
        self.binarray()
        print("> Constructing...")
        self.img = cv2.cvtColor(self.img,cv2.COLOR_GRAY2RGB)
        x = self.mazeinf[0]
        xt = 0
        while x < self.mazeinf[1]:
            y = self.mazeinf[2]
            yt = 0
            while y < self.mazeinf[3]:
                if [xt,yt] in self.res:
                    h,k = 0,0
                    k = self.mazeinf[4] + y if yt % 2 == 0 else self.mazeinf[5] + y
                    h = self.mazeinf[4] + x if xt % 2 == 0 else self.mazeinf[5] + x
                
                    self.img[x:h,y:k] = self.sol_clr    
                
                y += (self.mazeinf[4] if yt % 2 == 0 else self.mazeinf[5])
                yt += 1
            
            x += (self.mazeinf[4] if xt % 2 == 0 else self.mazeinf[5])
            xt += 1
        
        print("Showing Result.")
        return self.img

    def details(self):
        print("Under Dev.")