import cv2

def draw_line(rimg):
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    pt1 = (x1,y1)
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    pt2 = (x2,y2)
        
    cv2.line(rimg, pt1, pt2, (255,0,0), 2)
    
def draw_rectangle(rimg):
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    pt1 = (x1,y1)
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    pt2 = (x2,y2)
        
    cv2.rectangle(rimg, pt1, pt2, (255,0,0), 2)
    
def draw_circle(rimg):
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    centre = (x,y)
    radius = int(input("Entre radius: "))
        
    cv2.circle(rimg, centre, radius, (255,0,0), 2)
    
def draw_text(rimg):
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    org = (x,y)
    headingtxt = input("Entre the Heading Text: ")
        
    cv2.putText(rimg, headingtxt, org, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)