#export PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH
import sys
import cv2
import math
import numpy as np
import struct
import pickle 

from joblib import Parallel, delayed


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
	return mask_position;

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
	return features;

#creating tensor from mean color vector normalized
def creating_tensor_series(features, tensor_series, name_img):
	w, h = 3, 3;
	matrix = [[0 for x in range(w)] for y in range(h)]  
	matrix2 = [[0 for x in range(w)] for y in range(h)]

	for i in range(0,3):
		for j in range(0,3):
			matrix[i][j] = 0.0
			matrix2[i][j] = 0.0	

	for f in range(0,len(features)):
		for i in range(0,3):
			for j in range(0,3):  
				matrix[i][j] += features[f][i]*features[f][j]
		for i in range(0,3):
                        for j in range(0,3):
                                matrix2[i][j] += matrix[i][j]
	
	#normalizing l2 - each image has a tensor
	mean = 0.0
	for i in range(0,3):
               	for j in range(0,3):
                       	mean += matrix2[i][j]*matrix2[i][j]
		
        for i in range(0,3):
               	for j in range(0,3):
                       	matrix2[i][j] /= math.sqrt(mean)
		
	tensor_series.append(matrix2)
	
	name_img2 = name_img.split('/')
	name_file = 'tensor_from' + name_img2[3] + '.pkl'
	with open(name_file, 'wb') as file:
		pickle.dump({'tensor_series': tensor_series}, file)
	
	return tensor_series;


#accumulate temporal information 
def creating_final_tensor(tensor_series, final_tensor, mask, year, listpickle):
	mask = mask + year + ".tensor"
	print mask
	file = open(mask, "w")
	mean = 0.0

	for i in range(0,3):
		for j in range(0,3):
			final_tensor[i][j] = 0.0
	
	i = 0
	series = []
	with open(listpickle, 'r') as l:
		for line in l:
			pos = line.index('\n')
                        with open(line[0:pos], 'rb') as t:
				series.append(pickle.load(t)['tensor_series'])

	print len(series) 

	for f in range(0,len(series)):
		for i in range(0,3):
                        for j in range(0,3):
                                final_tensor[i][j] += float(series[f][i][j]) #tensor_series[f][i][j]
	
	#normalizing with l2			 
	for i in range(0,3):
                for j in range(0,3):
			mean += final_tensor[i][j]*final_tensor[i][j]
	
	for i in range(0,3):
        	for j in range(0,3):
	                final_tensor[i][j] /= math.sqrt(mean)
			file.write(str(final_tensor[i][j]) + ' ')
		file.write('\n')
	
	file.close()
	print final_tensor
	return;

def process(imagelist, i, features, mask_position, tensor_series):
	print imagelist[i]
	pos = imagelist[i].index('\n')
	img = cv2.imread(imagelist[i][0:pos])
	#extracting colors
	extracting_feature(features, mask_position, img)
	#creating tensor from mean color vector normalized
	creating_tensor_series(features, tensor_series,imagelist[i][0:pos])

#read mask
#read imagelist
mask = str(sys.argv[1])
images = str(sys.argv[2])
year = str(sys.argv[3])
listpickle = str(sys.argv[4])

print 'Working on mask', mask
print 'Working on observations', images

mask_img = cv2.imread(mask)
#cv2.imshow('image', mask_img)

imagelist = []
read_imagelist(images, imagelist)

print len(imagelist)

#separate mask
mask_position = [] 
extracting_mask(mask_img, mask_position)
features = [] 
tensor_series = []

w, h = 3, 3;
final_tensor = [[0 for x in range(w)] for y in range(h)]

#extract feature and create tensor
#for i in range(0, 100):
#for i in range(0,len(imagelist)):
#	process(imagelist, i, features, mask_position, tensor_series)
Parallel(n_jobs=1)(delayed(process)(imagelist, i, features, mask_position, tensor_series) for i in range(len(imagelist)))

#accumulate temporal information	
creating_final_tensor(tensor_series, final_tensor, mask,year, listpickle)
