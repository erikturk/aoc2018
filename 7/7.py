file= open('input','r')
source=file.readlines()
file.close()


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


g={allnodes[x].name:allnodes[x].after() for x in allnodes.keys()}

S = []
S_set = set()
index = {}
lowlink = {}
ret = []

def visit(v):
	index[v] = len(index)
	lowlink[v] = index[v]
	S.append(v)
	S_set.add(v)
	current=v
	for w in sorted(g.get(v,()),reverse=True):
		if w not in index:
			visit(w)
			lowlink[v] = min(lowlink[w],lowlink[v])
		elif w in S_set:
			lowlink[v] = min(lowlink[v], index[w])
	if lowlink[v] == index[v]:
		scc = []
		w = None
		while v != w:
			w = S.pop()
			scc.append(w)
			S_set.remove(w)
		ret.append(scc)
print('start')
for v in g:
	if not v in index:
		visit(v)

for i in sorted(list(allnodes.keys())):
	print(i,allnodes[i].after())

completed = list()
a = list()
n = list()

for i in allnodes.keys():
	print(i)
	if len(allnodes[i].after()) == 0:
		a.append(i)
	else:
		n.append(i)

available = list(sorted(a))

notready = list(sorted(n))

while len(available) > 0:
	last_letter_in_available = available.pop()
	completed.append(last_letter_in_available)

while len(notready) > 0:
	a = []
	not_ready_copy = list(notready)
	print('completed = ',completed)
	for i in not_ready_copy:
		if set(allnodes[i].after()).issubset(completed):
			a.append(i)
	available = list(sorted(a))
	print('Available = ',available)
	last_letter_in_available = available.pop()
	completed.append(last_letter_in_available)
	notready.remove(last_letter_in_available)
		
	print('notready = ',notready,'\n')
	
answer = "".join(list(reversed(completed)))
print(answer)

for line in source:
	if not answer.index(line.split(" ")[1]) < answer.index(line.split(" ")[7]):
		print(line)

available = list()
completed = list()
notready = list(reverse.keys())



while len(notready) > 0:
	a = []
	not_ready_copy = list(notready)
	print('completed = ',completed)
	for i in not_ready_copy:
		if set(reverse[i].after()).issubset(completed):
			a.append(i)
	available = list(sorted(a,reverse=True))
	print('Available = ',available)
	last_letter_in_available = available.pop()
	completed.append(last_letter_in_available)
	notready.remove(last_letter_in_available)
		
	print('notready = ',notready,'\n')

answer = "".join(list(completed))
print(answer)

for line in source:
	if not answer.index(line.split(" ")[1]) < answer.index(line.split(" ")[7]):
		print(line)
