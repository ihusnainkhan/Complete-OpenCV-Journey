import cv2
# print(cv2.__version__)
image = cv2.imread("Phase 1\Python-Logo.jpg") #imread = function to load image
if image is None:
    print("Error: Image not found.")
else:
    print("image loaded successfully")