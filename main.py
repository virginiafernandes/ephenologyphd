#export PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH
import sys
import cv2
import numpy as np

def read_imagelist(fname, imagelist):
	with open(fname, 'r') as f:
		for line in f:
			imagelist.append(line) 
	return;

def extracting_mask(mask_img, image, mask_position):
	i = 0
	j = 0
	npixels = 0;
	[a, b, c] = mask_img.shape
	for i in range(0, a):
		for j in range(0,b):
			color = mask_img[i,j,:]
			if color[0] == 255:
				mask_position.append([i,j])
	return;

def extracting_feature(feature, mask_position, img1):
	feature = [0,0,0]
	return;

#read mask
#read imagelist

mask = str(sys.argv[1])
images = str(sys.argv[2])

print 'Working on mask', mask
print 'Working on observations', images

mask_img = cv2.imread(mask)
#cv2.imshow('image', mask_img)

imagelist = []
read_imagelist(images, imagelist)

print imagelist[0][0:16]
img1 = cv2.imread(imagelist[0][0:16])

#separate mask + image
mask_position = []
extracting_mask(mask_img, img1, mask_position)

#extract feature
feature = [0,0,0]
extracting_feature(feature, mask_position, img1)
#transform feature vector into tensor

#accumulate temporal information 
