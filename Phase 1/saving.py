import cv2

image = cv2.imread("Phase 1\Python-Logo.jpg")
if image is not None:
    success = cv2.imwrite("Output-Python-Logo.jpg", image) #imwrite = save image after editing
    if success:
        print("Image saved successfully as 'Output-Python-Logo.jpg'")
    else:
        print("Failed to save an image.")
else:
    print("Error: Could not upload image.")