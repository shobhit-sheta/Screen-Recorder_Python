from PIL import ImageGrab   # manipulating, and saving many different image file formats
import numpy as np          # working with arrays
import cv2

# from win32api import GetSystemMetrics

# width = GetSystemMetrics(0)
# height = GetSystemMetrics(1)

width = 1920
height = 1080

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter('output.mp4', fourcc , 8, (width, height))

webcam = cv2.VideoCapture(0)
webcam.set(2, 100)
webcam.set(3, 100)

while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

    _, frame = webcam.read()
    fr_height, fr_width, _ = frame.shape
    img_final[0: fr_height, 0: fr_width, :] = frame[0: fr_height, 0: fr_width, :]

    # cv2.imshow('output', img_final)
    captured_video.write(img_final)
    if cv2.waitKey(10) == ord('q'):
        break