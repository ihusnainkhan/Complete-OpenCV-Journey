# ask file location from user input then give him multiple options whether they want 
# to draw line, circle, rectangle or want to write text over image. if he wants anything
# then ask for values for x,y give him output and ask they want to save or not.

import cv2

path = input("Entre your File Location:")
image = cv2.imread(path)
rimg = cv2.resize(image, (300,300))

choice = input("What did you want to draw?(Line/Rectangle/Circle/Text)\n")

if image is None:
    print("There's no image is uploaded")
    
else:
    if choice == "Line":
        x1 = int(input("Enter x1: "))
        y1 = int(input("Enter y1: "))
        pt1 = (x1,y1)
        x2 = int(input("Enter x2: "))
        y2 = int(input("Enter y2: "))
        pt2 = (x2,y2)
        
        cv2.line(rimg, pt1, pt2, (255,0,0), 2)
        cv2.imshow("Line Drawing", rimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # cv2.imwrite("line_draw.jpg",rimg)
        
    elif choice == "Rectangle":
        x1 = int(input("Enter x1: "))
        y1 = int(input("Enter y1: "))
        pt1 = (x1,y1)
        x2 = int(input("Enter x2: "))
        y2 = int(input("Enter y2: "))
        pt2 = (x2,y2)
        
        cv2.rectangle(rimg, pt1, pt2, (255,0,0), 2)
        cv2.imshow("Rectangle Drawing", rimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # cv2.imwrite("rectangle_draw.jpg",rimg)
        
    elif choice == "Circle":
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))
        centre = (x,y)
        radius = int(input("Entre radius: "))
        
        cv2.circle(rimg, centre, radius, (255,0,0), 2)
        cv2.imshow("Circle Drawing", rimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # cv2.imwrite("circle_draw.jpg",rimg)
        
    elif choice == "Text":
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))
        org = (x,y)
        headingtxt = input("Entre the Heading Text: ")
        
        cv2.putText(rimg, headingtxt, org, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)
        cv2.imshow("Text Drawing", rimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # cv2.imwrite("text_draw.jpg",rimg)
        
    else:
        print("It's any other function that is not explained here.")
        
save = input("Do you want to save? (y/n): ").lower()
if save == "y":
    cv2.imwrite("output.jpg", rimg)