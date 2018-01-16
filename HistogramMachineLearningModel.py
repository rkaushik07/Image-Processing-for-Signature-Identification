import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob, os
#img = cv2.imread('C:\\SDA\\SDA_Clean\\expsign27.png')
#img=cv2.imread('D:\\sample\\Signatures\\Signature16.png')

#val=np.convolve(hist[0],hist2[0],mode='full')
#print(val)

avg=0.9989878803211602
os.chdir("C:\\SDA\\SDA_Clean\\")
for file in glob.glob("*.png"):
    img=cv2.imread('C:\\SDA\\SDA_Clean\\'+str(file)+'')
    img2=cv2.imread('D:\\sample\\expsign27.png')
    hist=cv2.calcHist([img],[0],None,[256],[0,256])
    hist2=cv2.calcHist([img2],[0],None,[256],[0,256])
    retval=cv2.compareHist(hist,hist2,cv2.TM_CCORR_NORMED)
    print('  '+str(retval))
    if retval>=avg:
        print('Signature '+file)
    else:
        print('Other'+file)
#print(hist)
