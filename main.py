import sys
import cv2

#read mask
#read image

mask = str(sys.argv[1])
image = str(sys.argv[2])

print 'Working on mask', mask
print 'Working on observation', image

maskimg = cv2.imread(mask)
cv2.imshow('image', maskimg)

cv2.waitKey(0)
cv2.destroyAllWindows()

#separate mask + image

#extract feature

#transform feature vector into tensor

#accumulate temporal information 
