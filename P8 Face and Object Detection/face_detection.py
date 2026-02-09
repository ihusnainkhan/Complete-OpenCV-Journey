import cv2

face_cascade = cv2.CascadeClassifier("P8 Face and Object Detection\haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    # detectMultiScale = a function to scan & detect objects
    # 1.1 = scale factor: face find krna hai 10% zoom in krky hr dfa. 
    # mtlb ap dor ho to aik dfa zoom kya 10% phir jo frame ayi usko phir 10% zoom kiya until apka desired lvl na ajy face ko detect krny ka
    # 5 = minNeighbours: easy words ma hum 5 dfa test kr rhy hain or ya normal checking hai.
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        
    # (x,y) = top-left corner
    # (x+w, y+h) = bottom right corner
    
    # face[
    #     (100, 150, 80, 80) face1
    #     (250, 120, 90, 90) face2
    # ]
    # x = how far from left
    # y = how far from top
    # w = width of face
    # h = height of face
    
    cv2.imshow("Webcam Face Detection", frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
    