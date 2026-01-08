import cv2

image = cv2.imread("P3 Basic Image Drawing Techniques\Python-Logo.jpg")
rimg = cv2.resize(image, (300,300))

if rimg is None:
    print("The image is not uploaded.")
else:
    print("Image is Loaded")
    
    # cv2.circle(rimg, centre, radius, color, thickness) #general formula
    cv2.circle(rimg, (245,145), 40, (0,255,0), 2)
    
    cv2.imshow("Drawing circle",rimg)
    # cv2.imwrite("D_Circle_Image.jpg",rimg)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows