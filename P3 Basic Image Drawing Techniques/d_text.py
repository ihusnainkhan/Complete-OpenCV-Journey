import cv2

image = cv2.imread("P3 Basic Image Drawing Techniques\Python-Logo.jpg")
rimg = cv2.resize(image, (300,300))

if rimg is None:
    print("The image is not uploaded.")
else:
    print("Image is Loaded")
    
    # cv2.putText(rimg, text, org, font, fontscale, color, thickness) #general formula #org(x,y)
    cv2.putText(rimg, "This an official Python Logo", (30,40), 
                cv2.FONT_HERSHEY_PLAIN, 1.0, (255,0,0), 1)
    
    cv2.imshow("Writing Text Over Image",rimg)
    cv2.imwrite("Text_Over_Image.jpg",rimg)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows