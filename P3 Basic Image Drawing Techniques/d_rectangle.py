import cv2

image = cv2.imread("P3 Basic Image Drawing Techniques\Python-Logo.jpg")
rimg = cv2.resize(image, (300,300))

if rimg is None:
    print("The image is not uploaded.")
else:
    print("Image is Loaded")
    
    pt1 = (0,85)
    pt2 = (70,205)
    color = (0,0,255)
    thickness = 2 #if we set thickness value to -1 then it will fill the rectangle with clr.
    
    cv2.rectangle(rimg, pt1, pt2, color, thickness)
    
    cv2.imshow("Drawing rectangle",rimg)
    cv2.imwrite("D_Ractangle_Image.jpg",rimg)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows