import cv2

face_cascade = cv2.CascadeClassifier("P8 Face and Object Detection\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("P8 Face and Object Detection\haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("P8 Face and Object Detection\haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]
    # ROI = region of interest: basically ya slicing hai jo video ya image ma sy hamara 
    # ya wala area cut krdyn gi jo points hum usy dy rhy hain un points wala area.
    
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 5)
    if len(eyes) > 0:
        cv2.putText(frame, "Eyes Detected", (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)
        
    smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 30)
    if len(smiles) > 0:
        cv2.putText(frame, "Smiling", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)
        
    cv2.imshow("Smart Face Detector", frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
    