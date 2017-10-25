
#export PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH
import sys
import cv2
import math
import numpy as np

def read_imagelist(fname, imagelist):
        with open(fname, 'r') as f:
                for line in f:
                        imagelist.append(line)
        return;
#read mask
#read imagelist
mask1 = str(sys.argv[1])
mask2 = str(sys.argv[2])
mask3 = str(sys.argv[3])
images = str(sys.argv[4])

mask_img1 = cv2.imread(mask1)
height, width = mask_img1.shape[:2]
res = cv2.resize(mask_img1,(width/8, height/8), interpolation = cv2.INTER_CUBIC)      
cv2.imwrite(mask1, res)

mask_img2 = cv2.imread(mask2)
height, width = mask_img2.shape[:2]
res = cv2.resize(mask_img2,(width/8, height/8), interpolation = cv2.INTER_CUBIC)  
cv2.imwrite(mask2, res)

mask_img3 = cv2.imread(mask3)
height, width = mask_img3.shape[:2]
res = cv2.resize(mask_img3,(width/8, height/8), interpolation = cv2.INTER_CUBIC)  
cv2.imwrite(mask3, res)

imagelist = []
read_imagelist(images, imagelist)


for i in range(0,len(imagelist)):
        print imagelist[i][0:16]
        img = cv2.imread(imagelist[i][0:16])
	height, width = img.shape[:2]
	res = cv2.resize(img,(width/8, height/8), interpolation = cv2.INTER_CUBIC)
	cv2.imwrite(imagelist[i][0:16], res)
