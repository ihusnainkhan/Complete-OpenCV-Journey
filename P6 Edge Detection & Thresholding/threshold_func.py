import cv2

image = cv2.imread("P6 Edge Detection & Thresholding/flower.jpg", cv2.IMREAD_GRAYSCALE) 
# image must be in grayscale
rimg = cv2.resize(image, (300,500))

ret, thresh_image1 = cv2.threshold(rimg, 100, 255, cv2.THRESH_BINARY)
ret, thresh_image2 = cv2.threshold(rimg, 120, 255, cv2.THRESH_BINARY)
ret, thresh_image3 = cv2.threshold(rimg, 150, 255, cv2.THRESH_BINARY)

cv2.imshow("Original Image",rimg)
cv2.imshow("Edged Image 1", thresh_image1)
cv2.imshow("Edged Image 2", thresh_image2)
cv2.imshow("Edged Image 3", thresh_image3)

cv2.waitKey(0)
cv2.destroyAllWindows()