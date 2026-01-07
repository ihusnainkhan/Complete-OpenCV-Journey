import cv2

image = cv2.imread("Phase 1\Python-Logo.jpg")

if image is not None:
    h,w,c = image.shape #.shape is an attribute that prints height, width and color channels of the image. If image is greyscale it can only print 2 things height and width.
    print(f"Image Loaded:\nHeight: {h}\nWidth: {w}\nColor Channels: {c}")
else:
    print("Image not uploaded")