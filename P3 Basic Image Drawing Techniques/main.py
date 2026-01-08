import cv2
import drawing_utils

path = input("Entre your File Location:")
image = cv2.imread(path)
rimg = cv2.resize(image, (300,300))

choice = input("What did you want to draw?(Line/Rectangle/Circle/Text)\n").strip().lower()

if image is None:
    print("There's no image is uploaded")
    exit()
    
else:
    if choice == "line":
        drawing_utils.draw_line(rimg)
    elif choice == "rectangle":
        drawing_utils.draw_rectangle(rimg)
    elif choice == "circle":
        drawing_utils.draw_circle(rimg)
    elif choice == "text":
        drawing_utils.draw_text(rimg)
    else:
        print("Invalid option")
        
    cv2.imshow("Result", rimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
save = input("Do you want to save image? (yes/no): ").strip().lower()

if save == "yes":
    cv2.imwrite("output.jpg", rimg)
else:
    print("The program executes successfully")