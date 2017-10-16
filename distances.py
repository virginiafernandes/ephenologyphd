
import sys
import math

def l2_distance(distance, tensor1, tensor2):
	
	for i in range(0,3):
		for j in range(0,3):
			distance += (tensor1[i][j]-tensor2[i][j])*(tensor1[i][j]-tensor2[i][j])

	distance = math.sqrt(distance)
	return;


tensor1 =
tensor2 =
tensor3 = 

distance=0.0
l2_distance(distance, tensor1, tensor2)
print 't1,t2', distance

distance=0.0
l2_distance(distance, tensor1, tensor3)
print 't1,t3', distance
