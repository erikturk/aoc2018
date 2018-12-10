import sys
sys.setrecursionlimit(10**6)
file = open('input','r')
source = file.read()
file.close()

print(source)
stringinput = source.rstrip().split(' ')
input = [int(x) for x in stringinput]

#input = [1, 4, 0,1,9, 2, 3, 4, 5]
print(input)

def anychildren(start):
	if input[start] > 0:
		return True
	else:
		return False

def metadatalist(number,start):
	metalist = list()
	for i in range(number):
		metalist.append(input[start])
		start +=1
	
	return metalist,start

def check(start):
	num_meta = input[start+1]
	print('number of children: ',input[start],'number of metavariables',num_meta)
	if not anychildren(start):
		data,start = metadatalist(num_meta,start+2)
		metadata.extend(data)
	else:
		for i in range(input[start]):
			start = check(start+2)
		data, start = metadatalist(num_meta,start)
		metadata.extend(data)
	return start

#metadata=[]

#check(0)
#print(metadata)
#print(sum(metadata))

def sumtree(t):
	ch = t.pop(0)
	md = t.pop(0)
	return sum(sumtree(t) for _ in range(ch)) + sum(t.pop(0) for _ in range(md))

print (sumtree(input))
