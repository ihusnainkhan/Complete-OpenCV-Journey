import cv2

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_heigth = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')

# formula to record = cv2.VideoWriter(filename, codec, fps, frame_size)
# codec = compression format, fps = frame per second, frame_size = heigth & width of frames

recorder = cv2.VideoWriter("my_video.avi",codec,20,(frame_width,frame_heigth))

while True:
    success, image = camera.read()
    
    if success is not True:
        print("Could not find the frame")
        break
    
    recorder.write(image)
    cv2.imshow("Recording Live",image)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        print("Quitting...")
        break
    
camera.release()
recorder.release()
cv2.destroyAllWindows()