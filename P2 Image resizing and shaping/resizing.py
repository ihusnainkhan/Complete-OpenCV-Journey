import cv2

image = cv2.imread("P2 Image resizing and shaping\Python-Logo.jpg")

if image is None:
    print("Image is not uploaded")
else:
    print("Image Loaded")
    
    resized = cv2.resize(image, (300, 300)) #width & height: always remember first you put width and then height for resizing.
    
    cv2.imshow("Original Image",image)
    cv2.imshow("Resized Image",resized)
    
    cv2.imwrite("OP_Python_Logo.jpg",resized) #here always save new resized image else it will overlap.
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()