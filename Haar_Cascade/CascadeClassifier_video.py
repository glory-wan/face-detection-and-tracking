import cv2

eye_cascade = cv2.CascadeClassifier('../models/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in eyes:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('img', img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("\x1b"):
        break


cap.release()
cv2.destroyAllWindows()
