import cv2

webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Cannot open webcam")
    exit()

while True:
    ret, frame = webcam.read()
    
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow('Webcam', frame)
    
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break


webcam.release()
cv2.destroyAllWindows()