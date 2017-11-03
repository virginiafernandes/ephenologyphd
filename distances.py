import sys
import math
import numpy as np
import struct

class Tree:
	name = ''
	tensor=[[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]


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

fname = str(sys.argv[1]) #list of file of tensors for each mask
treenameslist = []#list of masks names
treetensors = []#list of tensors

read_list(fname, treenameslist)

for i in range(0, 2):#len(treenameslist)):
	#getting name
	pos = treenameslist[i].index('\n')
	tree_name = treenameslist[i][0:pos]
	tree = Tree()
	tree.name = tree_name
	#gettin tensor
	with open(tree.name, 'r') as f:
		s = f.read()
	s = s.split()
	pos = 0
	for a in range(0,3):
		for b in range(0,3):
			tree.tensor[a][b] = float(s[pos])
			pos = pos + 1		
	#saving tree
	treetensors.append(tree)

for i in range(0, len(treetensors)):
	#print treetensors[i].name
	print treetensors[i].tensor
