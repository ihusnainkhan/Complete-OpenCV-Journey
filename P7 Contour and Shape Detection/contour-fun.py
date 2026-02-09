import cv2

img = cv2.imread("P7 Contour and Shape Detection/triangle.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)

contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# cv2.drawcontours()
# general formula = cv2.drawContours(img, contours, contours_index, color, thickness)
# contour_index: 0 = first shape, 1 = second shape, -1 = all shapes in list

cv2.drawContours(img, contours, -1, (0,255,0), 2)

# General Formula
# approx = cv2.approxPolyDP(contour, epsilon, True)
# Epsilon = 0.01*arc length(contour, True) #0.01 the smaller = more precise, more points
# 0.01 the larger = rougher, fewer points # 0.01 is a turning parameter
# Epsilon identifies the simplified shape is how much closer to real one. smaller = accurate, larger = fewer points
# use arclength for epsilon. It adapt the size of new shape.
# if shape detection breaks u can use value 0.02 or 0.03 

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    corners = len(approx)
    
    if corners == 3:
        shape_name = "Triangle"
    elif corners == 4:
        shape_name = "Square"
    elif corners > 3:
        shape_name = "Circle"
    else:
        shape_name = "unknown"
    
    cv2.drawContours(img, [approx], 0, (0,255,0), 2)
    x = approx.ravel()[0] #Ravel = Converts multi dimensional array into 1D array.
    y = approx.ravel()[1] - 10
    cv2.putText(img, shape_name, (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,255,0), 2)    
    
cv2.imshow("Contours",img)
cv2.waitKey(0)
cv2.destroyAllWindows()