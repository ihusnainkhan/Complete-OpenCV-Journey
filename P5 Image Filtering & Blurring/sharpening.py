import cv2
import numpy as np
image = cv2.imread("P5 Image Filtering & Blurring\huanain'sheadshotblurred.png")
rimg = cv2.resize(image, (500,500))

sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])
# formula of sharpening = cv2.filter2D(image, depth, kernel_size)

sharpened = cv2.filter2D(rimg, -1, sharpen_kernel)

cv2.imshow("Original Image",rimg)
cv2.imshow("Blurred Image", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()