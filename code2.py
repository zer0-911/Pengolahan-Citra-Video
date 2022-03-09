import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

# # Cara susah untuk blur dengan kernel

# f = cv.imread('img/lenna.png')
# img = np.copy(f)
# f = np.double(cv.cvtColor(f, cv.COLOR_BGR2GRAY))/255
# b, k = f.shape
# fa = np.zeros([b, k])  # inisialisasi array dengan isi 0

# for i in range(1, b-1):
#     for j in range(1, k-1):
#         fa[i, j] = f[i, j]*1/9+f[i-1, j]*1/9+f[i+1, j]*1/9+f[i, j-1]*1/9+f[i,
#                                                                            j+1]*1/9+f[i-1, j-1]*1/9+f[i+1, j+1]*1/9+f[i-1, j+1]*1/9+f[i+1, j-1]*1/9

# cv.imshow('frame', f)
# cv.imshow('fa', fa)

# ch = cv.waitKey(0) & 0xFF
# cv.destroyAllWindows()

# # Cara sedikit tidak susah untuk blur dengan kernel

# f = cv.imread('img/lenna.png')
# img = np.copy(f)
# f = np.double(cv.cvtColor(f, cv.COLOR_BGR2GRAY))/255
# # LOW PASS FILTER Mengeluarkan tepi
# Kn = np.array([[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]])
# # HIGH PASS FILTER Memunculkan tepi
# Kn = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
# b, k = f.shape
# fa = np.zeros([b, k])  # inisialisasi array dengan isi 0
# for i in range(1, b-1):
#     for j in range(1, k-1):
#         for ii in range(-1, 2):
#             for jj in range(-1, 2):
#                 fa[i, j] = fa[i, j]+f[i+ii, j+jj]*Kn[ii+1, jj+1]


# cv.imshow('frame', f)
# cv.imshow('fa', fa)

# ch = cv.waitKey(0) & 0xFF
# cv.destroyAllWindows()
