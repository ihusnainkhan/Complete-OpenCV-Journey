import cv2

image = cv2.imread("P2 Image resizing and shaping\Python-Logo.jpg")

resizedimage = cv2.resize(image, (300,300))
if resizedimage is None:
    print("There's no image uploaded")
else:
    fliped_horizental = cv2.flip(resizedimage,1) #1 = flip in horizental
    fliped_vertical = cv2.flip(resizedimage,0) #0 = flip in vertical
    fliped_bothways = cv2.flip(resizedimage, -1) #-1 = flip in both horizental & vertical
    
    cv2.imshow("resized image", resizedimage)
    cv2.imshow("fliped Horizental",fliped_horizental)
    cv2.imshow("fliped Vertical",fliped_vertical)
    cv2.imshow("fliped Horizental & Vertical",fliped_bothways)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows