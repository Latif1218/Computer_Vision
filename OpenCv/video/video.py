import os
import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(BASE_DIR, "monkeyy.mp4")

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    raise IOError("Video file can't open")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    width = 640   
    height = 480  
    frame_resized = cv2.resize(frame, (width, height))

    cv2.imshow("Video", frame_resized)

    # press ESC to exit
    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()