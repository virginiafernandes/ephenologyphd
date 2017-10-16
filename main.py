import sys
import cv2

#read mask
#read image

mask = str(sys.argv[1])
imagelist = str(sys.argv[2])

print 'Working on mask', mask
print 'Working on observations', imagelist

maskimg = cv2.imread(mask)
#cv2.imshow('image', maskimg)


#separate mask + image

#extract feature

#transform feature vector into tensor

#accumulate temporal information 
