import os
import cv2

# read image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

img_path = os.path.join(BASE_DIR, "bird.jpg")




# write image

out_path = os.path.join(BASE_DIR, "bird_out.jpg")



img = cv2.imread(img_path)

if img is None:
    raise FileNotFoundError(f"Image not found: {img_path}")

cv2.imwrite(out_path, img)




# visualize image
cv2.imshow('image', img)
cv2.waitKey(5000)
