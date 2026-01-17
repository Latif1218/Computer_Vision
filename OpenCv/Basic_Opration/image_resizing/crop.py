# crop

import os
import cv2


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

img_path = os.path.join(BASE_DIR, "dogs1.jpg")



img = cv2.imread(img_path)

if img is None:
    raise FileNotFoundError(f"Image not found: {img_path}")

# resize_img = cv2.resize(img, (1280,960))
print(img.shape)

cropped_img = img[20:330, 200:460]

cv2.imshow('image', img)
cv2.imshow('cropimg', cropped_img)
cv2.waitKey(0)