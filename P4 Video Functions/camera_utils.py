import cv2

def live_webcam():
    camera = cv2.VideoCapture(0)
    while True:
        ret, frame = camera.read()
        if ret is not True:
            print("Could not find the frame")
            break
        
        cv2.imshow("Webcam Feed",frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            print("Quitting...")
            break
        
    camera.release()
    cv2.destroyAllWindows()
    
def record_webcam():
    camera = cv2.VideoCapture(0)
    
    frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_heigth = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
    codec = cv2.VideoWriter_fourcc(*'XVID')
    recorder = cv2.VideoWriter("video.avi",codec,20,(frame_width,frame_heigth))
    while True:
        ret, frame = camera.read()
        if ret is not True:
            print("Could not find the frame")
            break
        recorder.write(frame)
        cv2.imshow("Live Webcam Recording",frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
        
    camera.release()
    recorder.release()
    cv2.destroyAllWindows()
    
def saved_video():
    path = input("Entre your video path:")
    video = cv2.VideoCapture(path)
    
    while True:
        ret, frame = video.read()
        if ret is not True:
            break
        cv2.imshow("Saved Video Playing",frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
        
    video.release()
    cv2.destroyAllWindows()