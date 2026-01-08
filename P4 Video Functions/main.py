import cv2
import camera_utils

print("Welcome to Webcam Utility App")

print("Our Menu at Webcam Utility App")
print("1. Open webcam (Live view), \n2. Record webcam video, \n3. Play saved video, \n4. Exit")

while True:
    choice = int(input("Entre your preference by putting number:"))
    
    if choice == 4:
        print("The program executes successfully.")
        break
    
    else:
        if choice == 1:
            camera_utils.live_webcam()
        
        elif choice == 2:
            camera_utils.record_webcam()
        
        elif choice == 3:
            camera_utils.saved_video()
            
        else:
            print("Invalid option. Try again!")
            
        askuser = input("Did you want to continue?(Yes/No)").strip().lower()
        
        if askuser == "no":
            break
        else:
            continue
        
