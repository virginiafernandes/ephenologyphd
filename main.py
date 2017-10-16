#export PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH
import sys
import cv2
import numpy as np

def read_imagelist(fname, imagelist):
	with open(fname, 'r') as f:
		for line in f:
			imagelist.append(line) 
	return;

#extracting position from binary mask
def extracting_mask(mask_img, mask_position):
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

#R, G, B -> R/(R+G+B), G/(R+G+B), B/(R+G+B)
def extracting_feature(features, mask_position, img):
	features = []
	for i in range(0, len(mask_position)):
		[l,c] = mask_position[i]
		color = img[l,c,:]
		#R, G, B -> R/(R+G+B)
		mean = int(color[0])+int(color[1])+int(color[2])
		if mean > 0:
			color[0] /= mean
			color[1] /= mean
			color[2] /= mean
		features.append(color)
	return;

#creating tensor from mean color vector normalized
def creating_tensor_series(features, tensor_series):
		
	for f in range(0,len(features)):
		tensor_series.append(features[f]*transpose(features[f]))

	
	return;

#accumulate temporal information 
def creating_final_tensor(tensor_series, final_tensor):
	return final_tensor;


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

#separate mask
mask_position = []
extracting_mask(mask_img, mask_position)
features = []
tensor_series = []

#extract feature and create tensor
for i in range(0, 1):
#for i in range(0,len(imagelist)):
	print imagelist[i][0:16]
	img = cv2.imread(imagelist[i][0:16])
	#extracting colors
	extracting_feature(features, mask_position, img)
	#creating tensor from mean color vector normalized
	creating_tensor_series(features, tensor_series)
	#accumulate temporal information
	#creating_final_tensor(tensor_series)
