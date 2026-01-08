import cv2

image = cv2.imread("P5 Image Filtering & Blurring\husnain'sheadshot.png")
rimg = cv2.resize(image, (500,500))

# formula of median blurred = cv2.medianBlur(image, kernel_size)

blurred = cv2.medianBlur(rimg, 7)

cv2.imshow("Original Image",rimg)
cv2.imshow("Blurred Image", blurred)
cv2.waitKey(0)
cv2.imwrite("huanain'sheadshotblurred.png",blurred)
cv2.destroyAllWindows()