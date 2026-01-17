import os
import cv2


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

img_path = os.path.join(BASE_DIR, "cow.jpeg")



img = cv2.imread(img_path)

if img is None:
    raise FileNotFoundError(f"Image not found: {img_path}")


k_size = 5
img_blur = cv2.blur(img, (k_size, k_size))
img_gaussian_blur = cv2.GaussianBlur(img, (k_size, k_size), 3)
img_median_blur = cv2.medianBlur(img, k_size)

print(img.shape)
cv2.imshow('img', img)
cv2.imshow('img1', img_blur)
cv2.imshow('img2', img_gaussian_blur)
cv2.imshow('img3', img_median_blur)
cv2.waitKey(0)
