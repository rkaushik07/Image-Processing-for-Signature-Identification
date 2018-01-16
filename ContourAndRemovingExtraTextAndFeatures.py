import cv2
import numpy as np
import os.path
path = 'C:\\SDA\\SDA_Crop';
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
for file in range(num_files):

    #import image
    image = cv2.imread('C:\\SDA\\SDA_Crop\\crop'+str(file+1)+'.png')
    #cv2.imshow('orig',image)
    #cv2.waitKey(0)
    
    #grayscale
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #cv2.imshow('gray',gray)
    cv2.waitKey(0)
    
    #binary
    ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow('second',thresh)
    cv2.waitKey(0)
    
    #dilation
    kernel = np.ones((5,10), np.uint8)
    img_dilation = cv2.dilate(thresh, kernel, iterations=1)
    #cv2.imshow('dilated',img_dilation)
    cv2.waitKey(0)
    
    #find contours
    im2,ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    #sort contours
    sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
    
    for i, ctr in enumerate(sorted_ctrs):
        # Get bounding box
        x, y, w, h = cv2.boundingRect(ctr)
    
        # Getting ROI
        roi = image[y:y+h, x:x+w]
        if(h<50):
            # show ROI
            #cv2.imwrite('segment no:'+str(i) +".jpg",roi)
            cv2.rectangle(image,(x,y),( x + w, y + h ),(255,255,255),thickness=cv2.FILLED);
           # cv2.drawContours(roi,ctr,-1,(90,0,255),-1);
           # cv2.imwrite('D:\\pythonScripts\\temp\\segment no'+str(i) +".jpg",image)l,
            #emp = np.empty(roi.shape);
            #image[roi] = emp;
           # cv2.imshow('roi',roi);
         #   print(roi);
            #cv2.waitKey(0);
    cv2.imwrite("C:\\SDA\\SDA_Clean\\expsign"+str(file+1)+".png",image)
    #cv2.imshow('marked areas',image)

#cv2.waitKey(0)
