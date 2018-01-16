import cv2
import numpy as np
import math
import os
# Load the image
img = cv2.imread('C:\\SDA\\SDA_Image\\Original.png')
origY,origX=img.shape[:2];
img = cv2.resize(img,(1000,1000));
imgCpy = img;
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# convert to grayscale
# smooth the image to avoid noises
#gray = cv2.medianBlur(gray,5)
# Apply adaptive threshold

thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)
thresh_color = cv2.cvtColor(thresh,cv2.COLOR_GRAY2BGR)

# apply some dilation and erosion to join the gaps
thresh = cv2.dilate(thresh,None,iterations = 3)
thresh = cv2.erode(thresh,None,iterations = 2)

# Find the contours
_,contours,_ = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_TC89_L1)

i = 0;
# For each contour, find the bounding rectangle and draw it
for cnt in contours:
   
    x,y,w,h = cv2.boundingRect(cnt)
    #cv2.rectangle(imgCpy,(x,y),(x+w,y+h),(0,255,0),2)
   #cv2.rectangle(thresh_color,(x,y),(x+w,y+h),(0,255,0),2)
    roi = imgCpy[y:y+h,x:x+w];
    #cv2.imwrite('Region of Interest',roi);
    x=math.ceil((x*origX)/1000)-1;
    y=math.ceil((y*origY)/1000)-1;
    w=math.ceil((w*origX)/1000)-1;
    h=math.ceil((h*origY)/1000)-1;
    if(w>50):
        i=i+1;
        f=open('C:\\SDA\\SDA_Region\\Region'+str(i)+'.txt','w+');
        f.write(''+str(x)+' '+str(y)+' '+str(w)+' '+str(h));
        cv2.imwrite('C:\SDA\SDA_Dot\\Region'+str(i)+'.jpg',roi);
    cv2.waitKey(0);


# Finally show the image
#cv2.imshow('img',img)

#os.system("D:\\cropImage\\cropImage\\bin\\Debug\\cropimage.exe")
#cv2.imwrite('samplewordseg1.jpg',img);
#cv2.imshow('res',thresh_color)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
