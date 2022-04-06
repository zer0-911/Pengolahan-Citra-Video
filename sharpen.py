import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Mendapatkan frame
    ret, frame = cap.read()
    # jika frame terbaca maka ret
    if not ret:
        print("ERROR")
        break
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    image_sharp = cv.filter2D(src=frame, ddepth=-1, kernel=kernel)
    cv.imshow('frame', image_sharp)
    # Menampilkan hasil
    # Tekan q untuk exit
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
