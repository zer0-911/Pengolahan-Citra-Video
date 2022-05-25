import cv2 as cv
import numpy as np
import mediapipe as mp
# Menyimpan gambar latar belakang dalam daftar yang sudah dibuat.
bg_image = cv.imread("img/1.jpg")
mp_selfie_segmentation = mp.solutions.selfie_segmentation
selfie_segmentation = mp_selfie_segmentation.SelfieSegmentation(
    model_selection=1)
# Membuat objek video capture untuk membaca video dari kamera webcam.
cap = cv.VideoCapture(0)
while cap.isOpened():
    _, frame = cap.read()
    # Membalik frame ke arah horizontal
    frame = cv.flip(frame, 1)
    height, width, channel = frame.shape
    # Membuat objek frame yang akan dikirim ke mediapipe, sebelum itu dirubah dulu warna menjadi RGB.
    RGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    # Mendapatkan hasil
    results = selfie_segmentation.process(RGB)
    # extract segmented mask
    mask = results.segmentation_mask
    # Mengeluarkan output dari hasil segmentasi mask
    cv.imshow("mask", mask)
    key = cv.waitKey(1)
    if key == ord('q'):
        break
    condition = np.stack(
        (results.segmentation_mask,) * 3, axis=-1) > 0.5
    # Mengubah ukuran gambar latar belakang ke ukuran yang sama dengan frame asli
    bg_image = cv.resize(bg_image, (width, height))
    # menyatukan frame dengan background image (latar belakang)
    output_image = np.where(condition, frame, bg_image)
    cv.imshow("Output", output_image)
    cv.imshow("Frame", frame)
    if key == ord('q'):
        break
        # jika 'c' ditekan, maka gambar latar belakang akan diganti dengan gambar yang baru
    elif key == ord('c'):
        bg_image = cv.imread('img/quito.jpg')
