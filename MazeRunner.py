#Applicable Only for Orthogonal Mazes
import cv2 as cv ,time
from sys import setrecursionlimit
from lib_maze import solver

setrecursionlimit(10**6)

origimg = cv.imread('Maze/maze8.png')
(thresh, img) = cv.threshold(cv.cvtColor(origimg, cv.COLOR_BGR2GRAY), 127, 255, cv.THRESH_BINARY)

sol = solver(img)
start = time.time()
print("Under Development")
print("The process may take time, according to complexity and size of maze")

sol.getparam()
img = sol.construct()

end = time.time()
print("Execution Time :",end-start,"s")
cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()

print("Oops Something Is wrong")
