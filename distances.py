import sys
import math
import numpy as np
import struct

class Tree:
	def __init__(self,name, tensor):
		self.name = name
		self.tensor = tensor


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
w, h = 3, 3;
tensor = [[0 for x in range(w)] for y in range(h)]

read_list(fname, treenameslist)

for i in range(0,len(treenameslist)):
	#getting name
	pos = treenameslist[i].index('\n')
	tree_name = treenameslist[i][0:pos]
	#getting tensor
	with open(tree_name, 'r') as f:
		s = f.read()
	f.close()
	s = s.split()
	pos = 0
	for a in range(0,3):
		for b in range(0,3):
			tensor[a][b] = float(s[pos])
			pos = pos + 1
	#saving tree
	tree = Tree(tree_name, tensor)
	treetensors.append(tree)
	print treetensors[i].name
	print treetensors[i].tensor




