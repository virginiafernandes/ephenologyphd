
import sys
import math

def l2_distance(distance, tensor1, tensor2):
	
	for i in range(0,3):
		for j in range(0,3):
			distance += (tensor1[i][j]-tensor2[i][j])*(tensor1[i][j]-tensor2[i][j])

	distance = math.sqrt(distance)
	return;


tensor1 =
tensor2 = [[0.3349070137560781, 0.3341163465669872, 0.33331647084164523], [0.3341163465669872, 0.3333552245672337, 0.3325490372302122], [0.33331647084164523, 0.3325490372302122, 0.3317629522867682]]
tensor3 = [[0.2736673843078452, 0.3028133211906352, 0.3272098783286145], [0.3028133211906352, 0.3350869331976601, 0.36208095963347375], [0.3272098783286145, 0.36208095963347375, 0.3912713168319852]] 

distance=0.0
l2_distance(distance, tensor1, tensor2)
print 't1,t2', distance

distance=0.0
l2_distance(distance, tensor1, tensor3)
print 't1,t3', distance
