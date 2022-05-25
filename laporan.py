import numpy as np
import matplotlib.pyplot as plt
import cv2

# convo metode Pak Akok


def Conv2(f, kn):
    [nb, nc] = f.shape

    fa = np.zeros([nb, nc])

    for y in range(1, nb-1):
        for x in range(1, nc-1):
            for yy in range(-1, 2):
                for xx in range(-1, 2):
                    fa[y, x] = fa[y, x]+f[y+yy, x+xx]*kn[yy+1, xx+1]
    return np.copy(fa)


# f = cv2.imread('C:\VSC\Python\openCV\erwin.jfif')
f = cv2.imread('img/lenna.png')


# img=np.copy(f)

f = np.double(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY))/255

# kh =np.array([[0,-1,0],
#               [-1,4,-1],
#               [0,-1,0]])

k_lp = np.array([[0, -1, 0],
                 [-1, 2, 0],
                 [0, 0, 0]])

k_hp = np.array([[0, -1, 0],
                 [-1, 4, -1],
                 [0, -1, 0]])

k_sp = np.array([[0, -1, 0],
                 [-1, 5, -1],
                 [0, -1, 0]])

# convo metode openCV
img_sp = cv2.filter2D(src=f, ddepth=-1, kernel=k_sp)
img_hp = cv2.filter2D(src=f, ddepth=-1, kernel=k_hp)
img_lp = cv2.filter2D(src=f, ddepth=-1, kernel=k_lp)

cv2.imshow('f_sharpen_v2', img_sp)
cv2.imshow('f_lowpass_v2', img_lp)
cv2.imshow('f_highpass_v2', img_hp)


# fa = Conv2(f,k_lp)
# fb = Conv2(f,k_hp)
fc = Conv2(f, k_sp)

# fa= np.array(fa)
# fb= np.array(fb)
fc = np.array(fc)


# cv2.imshow('frame', f)
# cv2.imshow('f_low_pass', fa)
# cv2.imshow('fb_high_pass', fb)
cv2.imshow('f_sharpen', fc)

print(f.shape)

ch = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
