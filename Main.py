import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

cap = cv2.VideoCapture(0)


while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 4)


    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w , y+h), (255,255,255),2)

    cv2.imshow("img",img)

    k = cv2.waitKey(38)
    if k==27:
        break