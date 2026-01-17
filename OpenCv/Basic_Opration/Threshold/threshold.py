import os
import cv2


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

img_path = os.path.join(BASE_DIR, "bear.jpg")



img = cv2.imread(img_path)

if img is None:
    raise FileNotFoundError(f"Image not found: {img_path}")



img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)


cv2.imshow('img', img)
cv2.imshow('img1', img_gray)
cv2.imshow('img2', thresh)
cv2.waitKey(0)
