import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if ret is not True:
        print("Could not find the frame")
        break
    
    cv2.imshow("Webcam Feed",frame)
    
    if cv2.waitKey(1) & 0xff == ord('q'): #q is for quitting via keyboard. 
    #waitKey(1): It says u have to wait for 1 milli second to find out if there's any keyboard 
    #key is pressed to quit the program. If yes then it will break and print msg else it waits & observe.
        print("Quitting...")
        break
    
cap.release()
cv2.destroyAllWindows()