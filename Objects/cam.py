import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    flipped_frame = cv2.flip(frame, 1)
    cv2.imshow('Flipped Frame', flipped_frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
