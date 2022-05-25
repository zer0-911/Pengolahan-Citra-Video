from os import O_SYNC
import cv2 as cv
import numpy as np

# Penghapusan latar belakang warna dan mengganti dengan gambar latar belakang lain dengan video
# Membuat objek video capture untuk membaca video dari kamera webcam.
cap = cv.VideoCapture(0)

while True:
    # Mendapatkan frame setiap detik
    ret, frame = cap.read()
    # Mengubah warna frame menjadi halus
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    frame = cv.filter2D(src=frame, ddepth=-1, kernel=kernel)
    # kernel1 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
    # frame = cv.erode(frame, kernel1, iterations=2)
    # frame = cv.dilate(frame, kernel1, iterations=2)
    # Mengubah ke warna hsv
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    f2 = cv.imread('img/1.jpg')
    # Medapatkan ukuran dari frame
    b, c, d = frame.shape
    # Mengubah ukuran gambar latar belakang menjadi ukuran frame
    f2 = cv.resize(f2, (c, b), interpolation=cv.INTER_LINEAR)
    cv.imshow('f2resize', f2)
    # Menentukan lower dan upper bound warna (disini menggunakan warna merah)
    lower_bound = np.array([95, 100, 100], dtype=np.uint8)
    upper_bound = np.array([120, 255, 255], dtype=np.uint8)
    mask0 = cv.inRange(hsv, lower_bound, upper_bound)
    cv.imshow('mask0pertama', mask0)
    output_img1 = cv.bitwise_and(f2, f2, mask=mask0)
    cv.imshow('outputimg1', output_img1)
    # Membalik hasil mask
    mask1 = cv.bitwise_not(mask0)
    cv.imshow('mask1', mask1)
    output_img2 = cv.bitwise_and(frame, frame, mask=mask1)
    # Menggabungkan hasil dari output 1 dan 2
    fg = cv.add(output_img1, output_img2)
    cv.imshow('hsv', output_img2)
    cv.imshow('background', f2)
    cv.imshow('frame', fg)

    if cv.waitKey(1) == ord('q'):
        break
