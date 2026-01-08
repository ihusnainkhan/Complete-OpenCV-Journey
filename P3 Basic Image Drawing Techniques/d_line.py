import cv2

image = cv2.imread("P3 Basic Image Drawing Techniques\Python-Logo.jpg")
rimg = cv2.resize(image, (300,300))

if rimg is None:
    print("The image is not uploaded.")
else:
    print("Image is Loaded")
    
    pt1 = (20,200)
    pt2 = (279,200)
    color = (255,0,0)
    thickness = 2
    
    cv2.line(rimg, pt1, pt2, color, thickness)
    
    cv2.imshow("Drawing Line",rimg)
    cv2.imwrite("D_Line_Image.jpg",rimg)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows