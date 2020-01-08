
filepath = './dictionary.txt'

file = open(filepath, "r")

#temp = file.readline().splitlines()

def levenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

'''
s1 = 'apple'
s2 = 'apple'
print(levenshteinDistance(s1,s2))
'''


while True:
	file = open(filepath, "r")
	temp = file.readline()

	#print(temp)
	list = [[],[],[]]
	same = []
	flag = 0
	input1 = 'a'
	'''
	print("init")
	print(flag)
	print(list[0])
	print(list[1])
	print(list[2])
	'''



	input1 = input('Input the word you are looking for(0 exit)：')
	#print(input1)
	if input1 == "0":
		break;

	while temp:

		#print(temp)
		#print(len(temp))

		#temp = temp.splitlines()


		a = levenshteinDistance(input1,temp[:-1])
		if a == 0:
			same.append(temp)
			flag = 1;
			print("The word in the dictionary!")
			break;
		elif a == 1:

			list[0].append(temp[:-1])
			#print(temp)
		elif a == 2:
			list[1].append(temp[:-1])
			#print(temp)
		elif a == 3:
			list[2].append(temp[:-1])
			#print(temp)

		temp = file.readline()

	#print('flag' + str(flag))
	#print(same)
	if flag == 1:
		continue
	
	else:
		for j in range(0,3):
			print("edit_distance" + str(j+1) + ":")
			for i in range(len(list[j])):
				print(list[j][i])
	
		

	file.close()









