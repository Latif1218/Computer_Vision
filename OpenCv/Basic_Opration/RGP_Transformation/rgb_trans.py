# RGB Transformation

import os
import cv2


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

img_path = os.path.join(BASE_DIR, "bird3.jpg")



img = cv2.imread(img_path)

if img is None:
    raise FileNotFoundError(f"Image not found: {img_path}")

crop_img = img[120:550, 180:800]

img_rgb = cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB)
print(crop_img.shape)
# cv2.imshow('image1', img)
cv2.imshow('img1', crop_img)
cv2.imshow('img2', img_rgb)
cv2.waitKey(0)
