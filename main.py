import sys
import cv2

def read_imagelist(fname, imagelist):
	with open(fname, 'r') as f:
		for line in f:
			imagelist.append(line) 
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

print imagelist[0]
img1 = cv2.imread(imagelist[0])
cv2.imshow('image', img1)

#separate mask + image

#extract feature

#transform feature vector into tensor

#accumulate temporal information 
