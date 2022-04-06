import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


f_asli = cv.imread('img/lenna.png')
f = np.double(cv.cvtColor(f_asli, cv.COLOR_BGR2GRAY))/255
k_lp = np.array([[0, -1, 0],
                 [-1, 2, 0],
                 [0, 0, 0]])
f = cv.filter2D(src=f, ddepth=-1, kernel=k_lp)
cv.imshow('frame', f)
cv.imshow('frame2', f_asli)
ch = cv.waitKey(0) & 0xFF
cv.destroyAllWindows()
