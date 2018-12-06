file= open('testinput','r')
source=file.readlines()
file.close()

print(source)

class Node:

	def __init__(self,label):
		self.name=label
		self.after=list()

	def putin(self,predecessor):
		self.after.append(predecessor)

allnodes= dict()
for i in source:
	line = i.split(" ")
	print(line[1],line[7],allnodes.keys())
	if line[1] in allnodes:
		allnodes[line[1]].putin(line[7])
	else:
		allnodes[line[1]] = Node(line[1])
		allnodes[line[1]].putin(line[7])

	
for i in allnodes.keys():
	print(i,allnodes[i].after)	
