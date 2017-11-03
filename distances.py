import sys
import math
import numpy as np
import struct

def read_list(fname, treenameslist):
	with open(fname, 'r') as f:
		for line in f:
			treenameslist.append(line)
	return;

def l2_distance(tensor1, tensor2):
	distance = 0.0	
	for i in range(0,3):
		for j in range(0,3):
			distance += (tensor1[i][j]-tensor2[i][j])*(tensor1[i][j]-tensor2[i][j])

	distance = math.sqrt(distance)
	print distance
	return;

#tensor from each images are normalized. Then, its summation is also normalized.

fname = str(sys.argv[1]) #list of tensors for each mask

w,h = 3,3
tensor1 = [[0 for x in range(w)] for y in range(h)]
tensor2 = [[0 for x in range(w)] for y in range(h)]
treenameslist = []

read_list(fname, treenameslist)

for i in range(0, len(treenameslist)):
	pos = treenameslist[i].index('\n')
	tree_name = treenameslist[i][0:pos]
	print tree_name

print 't1,t2'
l2_distance(tensor1, tensor2)

