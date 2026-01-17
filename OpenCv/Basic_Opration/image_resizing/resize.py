# resizing

import os
import cv2


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

img_path = os.path.join(BASE_DIR, "dogs1.jpg")



img = cv2.imread(img_path)

if img is None:
    raise FileNotFoundError(f"Image not found: {img_path}")

resize_img = cv2.resize(img, (310, 175))

print(img.shape)
print(resize_img.shape)

cv2.imshow('image',resize_img)
cv2.waitKey(0)
cv2.imshow('image', img)
cv2.waitKey(0)

