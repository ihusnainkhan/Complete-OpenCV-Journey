import cv2

image = cv2.imread("P2 Image resizing and shaping\Python-Logo.jpg")

resizedimage = cv2.resize(image, (300,300))
if resizedimage is None:
    print("There's no image uploaded")
else:
    (h,w) = resizedimage.shape[:2] #basically 2 arg hoty hain h,w,c=colorscale but 
    #yahan 2 liya hain isliya hum ny slice krky btaya hai ky just 2 value chahiye.
    
    centre = (w//2, h//2) #this is a formula to find centre point of image.
    #w//2: // means divide the width by 2 so get centre horizentally. Same for height
    M = cv2.getRotationMatrix2D(centre, 90, 1.0) 
    #first argument = centre ya jahan sy stick krky rotate krwana ho
    #2nd argument = which angle did u want to rotate image.
    #3rd argument = zoom how much u wanted to zoom the image
    #So basically M becomes the formula for rotation then to get the output we will rotate by
    #warpAffine function.
    rotated = cv2.warpAffine(resizedimage, M, (w,h))
    #1st arg = original image
    #2nd arg = formula that we created
    #3rd arg = width and height of our image
    
    cv2.imshow("original image",resizedimage)
    cv2.imshow("rotated image",rotated)
    
    cv2.imwrite("OP_PL.jpg",rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows