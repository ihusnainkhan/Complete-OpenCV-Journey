import cv2

image = cv2.imread("Phase 1\Python-Logo.jpg")

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #cvtColor = convert colored image into grayscale.
    cv2.imshow("Grayscale Image",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Could not upload the image")