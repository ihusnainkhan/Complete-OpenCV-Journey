import cv2

image = cv2.imread("Phase 1\Python-Logo.jpg")
if image is not None:
    cv2.imshow("Image Showing", image) #imshow = to show the uploaded image
    cv2.waitKey(0) #waitKey = open the screen until we press any key 
    cv2.destroyAllWindows() #destroyAllWindows = as soon as we press any key the window shuts by itself.
else:
    print("Could not load the image.")