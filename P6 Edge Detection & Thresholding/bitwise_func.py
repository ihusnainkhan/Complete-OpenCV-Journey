# cv2.bitwise_and(img1, img2)
# cv2.bitwise_or(img1, img2)
# cv2.bitwise_not(img)

# * height and width of img 1 and img 2 must be same
# ** use only black and white

import cv2
import numpy as np

img1 = np.zeros((200,200), dtype="uint8")
img2 = np.zeros((200,200), dtype="uint8")

cv2.circle(img1, (80, 100), 50, 255, -1)
cv2.rectangle(img2, (100, 50), (180, 150), 255, -1)

bitwise_and = cv2.bitwise_and(img1, img2)
bitwise_or = cv2.bitwise_or(img1, img2)
bitwise_not = cv2.bitwise_not(img1)

cv2.imshow("Circle", img1)
cv2.imshow("Rectangle", img2)
cv2.imshow("AND", bitwise_and)
cv2.imshow("OR", bitwise_or)
cv2.imshow("NOT", bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()