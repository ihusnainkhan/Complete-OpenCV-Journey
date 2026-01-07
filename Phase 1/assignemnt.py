# Upload an image, convert it into grayscale, then show that pic and save it in your hard
# Challenges 1: take location of image from user input 
# 2: Ask user whether they want image to show or save 
# if they want to save the file then take the output name of file from user input.
# then display msg (file name saved successfully.)
import cv2

userinput = input("Entre your image location: ")

image = cv2.imread(userinput)
gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
    
choice = input("Do you want to show or save the image? (show/save): ")

if choice == "save":
    outputname = input("Entre your output file name: ")
    cv2.imwrite(outputname,gray)
    print(f"{outputname} saved successfully.")
elif choice == "show":
    cv2.imshow("Displaying Image",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Grayscale Image is displayed successfully.")
else:
    print("There's no image uploaded.")