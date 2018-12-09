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



import networkx as nx

G=nx.DiGraph()
for line in source:
	G.add_edge(line.split(' ')[1],line.split(' ')[7])
print(''.join(nx.lexicographical_topological_sort(G)))

task_times=[]
tasks=[]
time = 0
completed = list()

while task_times or G:
	available_tasks =[t for t in G if t not in tasks and G.in_degree(t) ==0]
	if available_tasks and len(task_times) < 5:
		task = min(available_tasks)
		task_times.append(ord(task) -4)
		tasks.append(task)
	else:
		min_time = min(task_times)
		completed = [tasks[i] for i,v in enumerate(task_times) if v == min_time]
		task_times = [ v- min_time for v in task_times if v > min_time]
		tasks = [t for t in tasks if t not in completed]
		time += min_time
		G.remove_nodes_from(completed)

print(time)
	
	
