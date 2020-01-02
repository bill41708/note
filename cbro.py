import re
import numpy as np
path = 't2.txt'
#從字串中讀數字
#T001:20,13,83,37,13,28,36,76,71,84,55,56,41,84,35,55,25,85,77,96,35,51,89
#[20, 13, 83, 37, 13, 28, 36, 76, 71, 84, 55, 56, 41, 84, 35, 55, 25, 85, 77, 96, 35, 51, 89]

file = open(path,"r")
temp = file.readline()

#print(temp)

i = 0
list1 = []

while(temp):
    #print(i)
    list1.append([])
    #print(list1)
    n = temp[5:]
    temp1 = re.findall(r"\d+\.?\d*",n)
    pp1 = np.array(temp1)


    for j in range(pp1.shape[0]):
        list1[i].append(int(temp1[j]))
        #print(list2[0])
        #print(list2[1])
    i += 1
    temp = file.readline()

print(i)
for j in range(i):
    print(list1[j])
