#export PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH
import sys
import cv2
import math
import numpy as np
import struct

def read_imagelist(fname, imagelist):
	with open(fname, 'r') as f:
		for line in f:
			imagelist.append(line) 
	return;

#extracting position from binary mask
def extracting_mask(mask_img, mask_position):
	i = 0
	j = 0
	[a, b, c] = mask_img.shape
	for i in range(0, a):
		for j in range(0,b):
			color = mask_img[i,j,:]
			if color[0] == 255:
				mask_position.append([i,j])
	return;

#R, G, B -> R/(R+G+B), G/(R+G+B), B/(R+G+B)
def extracting_feature(features, mask_position, img):
	color_float = [0.0,0.0,0.0]
	for i in range(0, len(mask_position)):
		[l,c] = mask_position[i]
		color = img[l,c,:]
		#R, G, B -> R/(R+G+B)
		mean = int(color[0])+int(color[1])+int(color[2])
		if mean > 0:
			color_float[0] = float(color[0]) / float(mean)
			color_float[1] = float(color[1]) / float(mean)
			color_float[2] = float(color[2]) / float(mean)
		features.append(color_float)
	return;

#creating tensor from mean color vector normalized
def creating_tensor_series(features, tensor_series):
	w, h = 3, 3;
	matrix = [[0 for x in range(w)] for y in range(h)]  

	for i in range(0,3):
		for j in range(0,3):
			matrix[i][j] = 0.0

	for f in range(0,len(features)):	
		mean = 0.0
		for i in range(0,3):
			for j in range(0,3):  
				matrix[i][j] += features[f][i]*features[f][j]
		#normalizing l2
		for k in range(0,3):
                	for l in range(0,3):
                        	mean += matrix[k][l]*matrix[k][l]

        	for k in range(0,3):
                	for l in range(0,3):
                        	matrix[k][l] /= math.sqrt(mean)

		tensor_series.append(matrix)	
	return;


#accumulate temporal information 
def creating_final_tensor(tensor_series, final_tensor, mask, year):
	mask = mask + year + ".tensor"
	print mask
	file = open(mask, "w")
	mean = 0.0

	for i in range(0,3):
		for j in range(0,3):
			final_tensor[i][j] = 0.0
			
	
	for f in range(0,len(tensor_series)):
		for i in range(0,3):
                        for j in range(0,3):
                                final_tensor[i][j] += tensor_series[f][i][j]
				 
	for i in range(0,3):
                for j in range(0,3):
			mean += final_tensor[i][j]*final_tensor[i][j]

	for i in range(0,3):
        	for j in range(0,3):
	                final_tensor[i][j] /= math.sqrt(mean)
			file.write(str(final_tensor[i][j]) + ' ')
		file.write('\n')


	#s = struct.pack('d'*len(final_tensor), *final_tensor)
	#file.write(final_tensor)
	
	file.close()
	print final_tensor
	return;


#read mask
#read imagelist
mask = str(sys.argv[1])
images = str(sys.argv[2])
year = str(sys.argv[3])

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

w, h = 3, 3;
final_tensor = [[0 for x in range(w)] for y in range(h)]

#extract feature and create tensor
for i in range(0, 100):
#for i in range(0,len(imagelist)):
	print imagelist[i]
	pos = imagelist[i].index('\n')
	img = cv2.imread(imagelist[i][0:pos])
	#extracting colors
	extracting_feature(features, mask_position, img)
	#creating tensor from mean color vector normalized
	creating_tensor_series(features, tensor_series)

#accumulate temporal information	
creating_final_tensor(tensor_series, final_tensor, mask,year)
