import cv2

image = cv2.imread("P2 Image resizing and shaping\Python-Logo.jpg")

if image is not None:
    # this is extra u can check ur image dimesions by using image.shape function
    # h,w,c = image.shape
    # print(f"Height: {h},\nWidth: {w},\nColor Channels: {c}")
    
    # cropped = image[starty:endy,startx:endx]
    cropped = image[450:850, 330:770]
    
    cv2.imshow("Original Image",image)
    cv2.imshow("Cropped Image",cropped)
    
    cv2.imwrite("OP_Python_Logo.jpg",cropped) #here always save new resized image else it will overlap.
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image is not uploaded.")