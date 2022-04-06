import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


def Conv2(f, kn):
    [nb, nc] = f_asli.shape
    fa = np.zeros([nb, nc])

    for y in range(1, nb-1):
        for x in range(1, nc-1):
            for yy in range(-1, 2):
                for xx in range(-1, 2):
                    fa[y, x] = fa[y, x]+f[y+yy, x+xx]*kn[yy+1, xx+1]
    return np.copy(fa)


f_asli = cv.imread('img/lenna.png')
f = np.double(cv.cvtColor(f_asli, cv.COLOR_BGR2GRAY))/255
k_cv = np.array([[0, -1, 0],
                 [-1, 5, -1],
                 [0, -1, 0]])

fc = Conv2(f, k_cv)
cv.imshow('frame', f)
cv.imshow('frame2', f_asli)
ch = cv.waitKey(0) & 0xFF
cv.destroyAllWindows()
