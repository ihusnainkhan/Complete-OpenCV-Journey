import cv2

image = cv2.imread("P5 Image Filtering & Blurring\husnain'sheadshot.png")

# General Formula Gaussian Blur = cv2.GaussianBlur(src=image, (kernel_size_x,kernel_size_y), sigma)
# kernel window values must be in odd number always. e.g(3,3)
# it's like a grid main ma ap hogy and usky around jo values hon gi unka sum krky average ly kr 
# apky sath replace kr diya jyga like 3x3. centre value is you and around that we have 8 values
# hum un 8 values ka average ly kr you ki jo value hai us sy replace krdyn gy so it can blend smoothly.
# inshort iska mtlb ya hota hai ky how much u want to blur the image.

# sigma = if 0 opencv will decide itself how much blur to put in image.
blurred = cv2.GaussianBlur(image, (7,7), 0)

cv2.imshow("Original Image",image)
cv2.imshow("Blurred Image",blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()