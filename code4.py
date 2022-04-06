import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

# # Penghapusan warna (pengecekan sesuai warna)
# f = cv.imread('img/bunga.jpeg')
# hsv = np.double(cv.cvtColor(f, cv.COLOR_BGR2HSV))

# lower_bound = np.array([90, 0, 0], dtype=np.uint8)
# upper_bound = np.array([150, 255, 255], dtype=np.uint8)
# mask = cv.inRange(hsv, lower_bound, upper_bound)
# mask0 = cv.bitwise_not(mask)
# output_img1 = cv.bitwise_and(f, f, mask=mask0)

# cv.imshow('frame', f)
# cv.imshow('mask', mask)
# cv.imshow('mask1', output_img1)

# ch = cv.waitKey(0) & 0xFF
# cv.destroyAllWindows()

# # Penghapusan warna dengan video
# cap = cv.VideoCapture(0)

# while True:
#     # Mendapatkan frame setiap detik
#     ret, frame = cap.read()
#     hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

#     lower_bound = np.array([90, 0, 0], dtype=np.uint8)
#     upper_bound = np.array([150, 255, 255], dtype=np.uint8)
#     mask = cv.inRange(hsv, lower_bound, upper_bound)
#     mask0 = cv.bitwise_not(mask)
#     output_img1 = cv.bitwise_and(frame, frame, mask=mask0)

#     cv.imshow('frame', output_img1)

#     if cv.waitKey(1) == ord('q'):
#         break
# cap.release()
# cv.destroyAllWindows()

# # Penghapusan warna dan mengganti dengan gambar lain metode saya
# f = cv.imread('img/bunga.jpeg')
# f2 = cv.imread('img/its.jpg')
# print('This image is:', type(f),
#       ' with dimensions:', f.shape)
# hsv = np.double(cv.cvtColor(f, cv.COLOR_BGR2HSV))
# height, width, channels = f.shape
# down_points = (width, height)
# resized_down = cv.resize(f2, down_points, interpolation=cv.INTER_LINEAR)
# lower_bound = np.array([90, 0, 0], dtype=np.uint8)
# upper_bound = np.array([150, 255, 255], dtype=np.uint8)
# mask = cv.inRange(hsv, lower_bound, upper_bound)
# mask0 = cv.bitwise_not(mask)
# output_img1 = cv.bitwise_and(f, f, mask=mask0)
# background_image = cv.cvtColor(f2, cv.COLOR_BGR2RGB)
# crop_background = background_image[0:height, 0:width]

# crop_background[mask == 0] = [0, 0, 0]
# complete_image = output_img1 + crop_background

# cv.imshow('gambarasli', f)
# cv.imshow('resizeimage', resized_down)
# cv.imshow('maskingimage', output_img1)
# cv.imshow('gambarjadi', complete_image)

# ch = cv.waitKey(0) & 0xFF
# cv.destroyAllWindows()

# # Penghapusan warna dan mengganti dengan gambar lain metode bapak akok
# f = cv.imread('img/bunga.jpeg')
# f2 = cv.imread('img/its.jpg')
# b, c, d = f.shape
# hsv = np.double(cv.cvtColor(f, cv.COLOR_BGR2HSV))
# f2 = cv.resize(f2, (c, b), interpolation=cv.INTER_LINEAR)
# lower_bound = np.array([90, 0, 0], dtype=np.uint8)
# upper_bound = np.array([150, 255, 255], dtype=np.uint8)
# mask0 = cv.inRange(hsv, lower_bound, upper_bound)

# output_img1 = cv.bitwise_and(f2, f2, mask=mask0)
# mask1 = cv.bitwise_not(mask0)
# output_img2 = cv.bitwise_and(f, f, mask=mask1)
# fg = cv.add(output_img1, output_img2)


# cv.imshow('gambarasli', f)
# cv.imshow('gambarjadi', fg)
# ch = cv.waitKey(0) & 0xFF
# cv.destroyAllWindows()
