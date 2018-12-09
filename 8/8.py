file = open('testinput','r')
source = file.read()
file.close()

print(source)
stringinput = source.rstrip().split(' ')
input = [int(x) for x in stringinput]


input = [1, 4, 0,1,9, 2, 3, 4, 5]
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

def check(input):
	start=1
	num_meta = input[1]
	if input[0] == 0: # number of children = 0
		metadata.extend(input[2:2+num_meta])
		newinput = input[2:2+num_meta]
	
		print('number of children: ',input[0],'number of metavariables',num_meta,"metas =",input[-num_meta:])
	else:
		# now comes a number of children.
		# we have to keep track of the number of children, because
		# at the end, there's some metadata for this level we have to collect.
		print(input)
		for i in range(input[0]):
			newinput = check(input[2:])

	return newinput

	

metadata=[]

while len(input) >0:
	input = check(input)
print(metadata)
print(sum(metadata))
