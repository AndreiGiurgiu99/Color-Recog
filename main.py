import numpy as np
import pandas as pd
import cv2
from tkinter import filedialog as fd

try:
    img = cv2.imread(fd.askopenfilename()) #read the image file  
except OSError as e:
    quit()


index = ["color", "hex", "R", "G", "B"] #colum names

try:
    csv = pd.read_csv('Culori.csv', names=index, header=None) #read csv file in pandas dataframe
except OSError as e:
    quit()
    
clicked = False
r = g = b = xpos = ypo = 0


#### COLOR RECOGNITION FUNCTION ####

def recognize_color(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
         d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
         
         if (d <= minimum):
            minimum = d
            cname = csv.loc[i,"color"]
            chex  = csv.loc[i,"hex"]
    return cname


#### CLICK FUNCTION ####

def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos,clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]

        b = int(b)
        g = int(g)
        r = int(r)


#### UI APPLICATION ####

cv2.namedWindow('Recunoastere culoare Pantone')

cv2.setMouseCallback('Recunoastere culoare Pantone', mouse_click)

try:
    while(1):
        cv2.imshow("Recunoastere culoare Pantone", img)
        if (clicked):

            cv2.rectangle(img, (20,20), (750,60), (b,g,r), -1)

            text = recognize_color(r,g,b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

            cv2.putText(img, text, (50,50), 2, 0.8, (255,255,255), 2 , cv2.LINE_AA)

            if (r+g+b >= 600):
                cv2.putText(img, text, (50,50), 2, 0.8, (0,0,0), 2, cv2.LINE_AA)

            clicked = False
        
        if cv2.waitKey(20) & 0xFF == 27:
            cv2.destroyAllWindows()
            break

except OSError as e:
    quit()