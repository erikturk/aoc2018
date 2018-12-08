file= open('testinput','r')
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
completed = list()
a = list()
available = list()
completed = list()
notready = list(reverse.keys())

while len(notready) > 0:
	a = []
	not_ready_copy = list(notready)
	#print('completed = ',completed)
	for i in not_ready_copy:
		if set(reverse[i].after()).issubset(completed):
			a.append(i)
	available = list(sorted(a,reverse=True))
	#print('Available = ',available)
	last_letter_in_available = available.pop()
	completed.append(last_letter_in_available)
	notready.remove(last_letter_in_available)
		
	#print('notready = ',notready,'\n')

answer = "".join(list(completed))

for line in source:
	if not answer.index(line.split(" ")[1]) < answer.index(line.split(" ")[7]):
		print("Error:",line)

workers = 2
totaltime = ord(completed[0])-64+60

todo = completed
done=[completed[0]]
todo.remove(completed[0])
available=list()
next_end_time = [0:2,totaltime:2]

workers_available = workers
while len(done) < len(completed):
	a=list()
	todo_copy = list(todo)
	for i in todo_copy:
		if set(reverse[i].after()).issubset(done):
			a.append(i)
	available = list(sorted(a,reverse=True))
	while workers_available <= workers:
		if len(available) > 0:
			job = available.pop()
			totaltime i+= ord(job)-64+60
			next_end_time.append(totaltime:1)
	
	
print(done)
	
