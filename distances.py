import sys
import math
import numpy as np
import struct

class Tree:
	def __init__(self, name, tensor, distance):
		self.name = name
		self.tensor = tensor
		self.distance = distance


def read_list(fname, treenameslist):
	with open(fname, 'r') as f:
		for line in f:
			treenameslist.append(line)
	return;

def l2_distance(tensor1, tensor2, distance):
	distance[0] = 0.0	
	for i in range(0,3):
		for j in range(0,3):
			distance[0] += (tensor1[i][j]-tensor2[i][j])*(tensor1[i][j]-tensor2[i][j])

	distance[0] = math.sqrt(distance[0])
	#print distance
	return;

def read_treetensors(treenameslist, treetensors):
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
        	w, h = 3, 3
		tensor = [[0 for x in range(w)] for y in range(h)]
        	for a in range(0,3):
                	for b in range(0,3):
                        	tensor[a][b] = float(s[pos])
                        	pos = pos + 1
        	#saving tree
        	tree = Tree(tree_name, tensor, 999.0)
        	treetensors.append(tree)

#tensor from each images are normalized. Then, its summation is also normalized.
#comparing by year
fname1 = str(sys.argv[1]) #list of file of tensors for each mask
fname2 = str(sys.argv[2]) #list of file of tensors for each mask
treenameslist1 = []#list of masks names
treenameslist2 = []#list of masks names
treetensors1 = []#list of tensors 1
treetensors2 = []#list of tensors 2

treetensorsforsort = [] #result in order

read_list(fname1, treenameslist1)
read_list(fname2, treenameslist2)

read_treetensors(treenameslist1, treetensors1)
read_treetensors(treenameslist2, treetensors2)


for i in range(0, len(treetensors1)):
	for j in range(0, len(treetensors2)):
		distance = [0,0]
		#print treetensors1[i].name + ' ' + treetensors2[j].name
		l2_distance(treetensors1[i].tensor, treetensors2[j].tensor, distance)
		treetensors2[j].distance = distance[0]
	treetensorsforsort = treetensors2
	treetensorsforsort = sorted(treetensorsforsort, key=lambda tree: tree.distance)
	for j in range(0, len(treetensorsforsort)):
		print treetensors1[i].name + ' ' + treetensorsforsort[j].name
		print treetensorsforsort[j].distance	

