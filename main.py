import sys
import cv2

def read_imagelist(str):
	print str 
	return;

#read mask
#read imagelist

mask = str(sys.argv[1])
imagelist = str(sys.argv[2])

print 'Working on mask', mask
print 'Working on observations', imagelist

maskimg = cv2.imread(mask)
#cv2.imshow('image', maskimg)

read_imagelist(imagelist)

#separate mask + image

#extract feature

#transform feature vector into tensor

#accumulate temporal information 
