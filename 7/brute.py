file= open('input','r')
source=file.readlines()
file.close()

print(source)

class Node:

	def __init__(self,label):
		self.name=label
		self.successors=list()
		self.innum=0
		self.outnum=0

	def putin(self,predecessor):
		self.successors.append(predecessor)

	def after(self):
		return sorted(list(self.successors))

allnodes= dict()
reverse=dict()
for i in source:
	line = i.split(" ")
	print(line[1],line[7],allnodes.keys())
	if line[1] in allnodes:
		allnodes[line[1]].putin(line[7])
	else:
		allnodes[line[1]] = Node(line[1])
		allnodes[line[1]].putin(line[7])
	if line[7] not in allnodes:
		allnodes[line[7]] = Node(line[7])

	if line[7] in reverse:
		reverse[line[7]].putin(line[1])
	else:
		reverse[line[7]] = Node(line[7])
		reverse[line[7]].putin(line[1])
	
	if line[1] not in reverse:
		reverse[line[1]] = Node(line[1])

for i in sorted(list(allnodes.keys())):
	print(i,allnodes[i].after())

