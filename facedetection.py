import cv2

face_cascade = cv2.CascadeClassifier('C:/Users/KIIT/cloudclouse/facedetection.py/raw.githubusercontent.com_adarsh1021_facedetection_master_haarcascade_frontalface_default (1).xml')

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (225, 0, 0), 2)

    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

