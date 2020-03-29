#Applicable Only for Rectangle-Cell Mazes
import cv2,time
from sys import setrecursionlimit
from easygui import fileopenbox
from lib_maze import solver
#from termcolor import colored
setrecursionlimit(10**6)

#adjust location as per your convenience
try:
    img_path = fileopenbox()
    origimg = cv2.imread(img_path)
    (thresh, img) = cv2.threshold(cv2.cvtColor(origimg, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)

    sol = solver(img)
    start = time.time()
    print("Under Development")

    print("The process may take time, according to complexity and size of maze")

    sol.normalise()
    img = sol.construct()

    end = time.time()
    print("Execution Time :",end-start,"s")
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    print("Oops Something Is wrong")
