# Test code for Grand Challenge. The evaluation metric is mAP
# In grand challenge, we do not provide or consider the camera id information.
import sys
import os
import numpy as np 
import cv2


path1 = sys.argv[1] # GT
path2 = sys.argv[2] # results
flag = int(sys.argv[3]) # 1 for suffix, 0 for no suffix 

f1 = open(path1, "r")

line  = f1.readline()

D = {}
cnt = 0
while line:

	line = line.strip()
	tmp = line.split(' ')
	kk = tmp[0]
	L = []
	for i in range(1, len(tmp)):
		L.append(tmp[i])
	D[kk] = L
	cnt +=1
	line = f1.readline()
f1.close()

f2 = open(path2, "r")
total_AP = 0
line  = f2.readline()
while line:
	line  = line.strip()
	tmp = line.split(' ')
	query_num = tmp[0]
	if flag == 1:
		query_num = query_num.split('.')[0]
	AP = 0
	cnt2 = 1
	for i in range(1, len(tmp)):
		res = tmp[i]
		if flag == 1:
			res = res.split('.')[0]
		if res in D[query_num]:
			AP += (cnt2 * 1.0 ) / i
			cnt2 +=1
	if cnt2 == 1:
		AP = 0
	else:
		AP = AP * 1.0 / (cnt2-1)
	total_AP += AP
	line = f2.readline()
f2.close()
MAP = total_AP * 1.0 /cnt
print(MAP)
