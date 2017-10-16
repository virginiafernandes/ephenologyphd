#export PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH
import sys
import cv2
import numpy as np

def read_imagelist(fname, imagelist):
	with open(fname, 'r') as f:
		for line in f:
			imagelist.append(line) 
	return;

def extracting_mask(new_img, mask_img, image):
	x = 0
	i = 0
	j = 0
	[a, b, c] = mask_img.shape
	mask_position =[]
	for i in range(0, a):
		for j in range(0,b):
			color = mask_img[i,j,:]
			if color[0] == 255:
				mask_position.append([i,j])
				x += 1
	#new_img = cv2.resize(new_img, (x, y))
	#new_img = imwrite('testing.jpg', new_img)
	return;


#read mask
#read imagelist

mask = str(sys.argv[1])
images = str(sys.argv[2])

print 'Working on mask', mask
print 'Working on observations', images

maskimg = cv2.imread(mask)
#cv2.imshow('image', maskimg)

imagelist = []
read_imagelist(images, imagelist)

print imagelist[0][0:16]
img1 = cv2.imread(imagelist[0][0:16])
#cv2.imshow('image', img1)

#separate mask + image
new_img = cv2.imread('testing.jpg')
extracting_mask(new_img, maskimg, img1)


#extract feature

#transform feature vector into tensor

#accumulate temporal information 
