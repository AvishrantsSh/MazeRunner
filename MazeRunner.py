import cv2
import numpy as np

def normalise(img, dim):
    for x in range(0,dim[0]):
        for y in range(0,dim[1]):
            if np.any(img[x][y] != 255) and np.any(img[x][y] != 0):
                img[x][y] = [0,0,0]

#adjust location as per your convenience
img = cv2.imread("/home/avishrant/GitRepo/MazeRunner/maze.png")
dim = img.shape
normalise(img,dim)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
