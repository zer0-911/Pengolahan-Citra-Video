import numpy as np
from matplotlib import pyplot as plt
import cv2

# img = cv2.imread('img/lena.jpg', 0)
# #im = np.double(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))/255
# # c=0.7


# # for i in range(im.shape[0]):
# #    for j in range(im.shape[1]):
# #        im[i,j]=im[i,j]+c


# #im = im+c


# cv2.imshow('frame', img)

# ch = cv2.waitKey(0) & 0xFF

# # Cara susah untuk membuat warna abu-abu
# img = np.double(cv2.imread('img/lenna.png'))/255
# imb = np.zeros([512, 512, 3])

# for i in range(512):
#     for j in range(512):
#         w = (img[i, j, 0]+img[i, j, 1]+img[i, j, 2])/3
#         imb[i, j, 0] = w
#         imb[i, j, 1] = w
#         imb[i, j, 2] = w
#
#         imb2[i,j]=w;
# # imb shape dikali 3 karena RGB -> (512,512)
# # imb shape -> (512,512,3)

# cv2.imshow('frame1', img)
# cv2.imshow('frame2', imb)
# ch = cv2.waitKey(0) & 0xFF
# cv2.destroyAllWindows()


# # Cara gampang untuk membuat warna abu-abu
# img = cv2.imread('img/lenna.png')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('frame1', img)

# ch = cv2.waitKey(0) & 0xFF
# cv2.destroyAllWindows()

# # Cara susah untuk mengatur brightness
# img = np.double(cv2.imread('img/lenna.png'))/255
# imb = np.zeros([512, 512, 3])
# imbri = np.zeros([512, 512, 3])
# c = 0.5
# for i in range(512):
#     for j in range(512):
#         imbri[i, j, 0] = img[i, j, 0] + c
#         imbri[i, j, 1] = img[i, j, 1] + c
#         imbri[i, j, 2] = img[i, j, 2] + c


# cv2.imshow('frame1', img)
# cv2.imshow('frame3', imbri)
# ch = cv2.waitKey(0) & 0xFF
# cv2.destroyAllWindows()

# # Cara gampang untuk mengatur brightness
# img = cv2.imread('img/lenna.png')
# img = np.double(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))/255
# c = 0.5
# imbr = img-c
# cv2.imshow('frame1', img)
# cv2.imshow('frame2', imbr)
# ch = cv2.waitKey(0) & 0xFF
# cv2.destroyAllWindows()

# # Cara gampang untuk mengatur kontras
img = cv2.imread('img/lenna.png')
f = np.double(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))/255
b = 0.4
alpha = 2
fa = (f-b)*alpha+b
cv2.imshow('frame', img)
cv2.imshow('frame1', f)
cv2.imshow('frame2', fa)
ch = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
