import cv2

image = cv2.imread("P6 Edge Detection & Thresholding/flower.jpg", cv2.IMREAD_GRAYSCALE) 
# image must be in grayscale
rimg = cv2.resize(image, (300,500))

edges = cv2.Canny(rimg, 120, 200)

cv2.imshow("Original Image",rimg)
cv2.imshow("Edged Image", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()