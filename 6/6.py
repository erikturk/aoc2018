file = open("input","r")
source= file.readlines()
file.close()
input=list()


class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.distances = dict()

	def closestpoint(self):
		return

for i in source:
	input.append((int(i.split(",")[0]),int(i.split(",")[1])))
	
allpoints = dict()

xmax = max([x[0] for x in input])
xmin = min([x[0] for x in input])

ymax = max([x[1] for x in input])
ymin = min([x[1] for x in input])
print(xmin,xmax,"y:",ymin,ymax)

for x in range(xmin,xmax+1):
	for y in range(ymin,ymax+1):
		closest_distance = 2*(max([xmax,ymax])+1)
		closest_point = (-1,-1)
		for p in input:
			if abs(x-p[0])+abs(y-p[1]) <= closest_distance:
				if abs(x-p[0])+abs(y-p[1]) == closest_distance:
					closest_point = (10000,10000)
				else:	
					closest_distance = abs(x-p[0])+abs(y-p[1])
					closest_point = p
		allpoints[(x,y)] = closest_point  

blacklist=set()

for x in range(xmin,xmax):
	
	if allpoints[(x,ymin)] in input:
		blacklist.add(allpoints[(x,ymin)])
	if allpoints[(x,ymax)] in input:
		blacklist.add(allpoints[(x,ymax)])

for y in range(ymin,ymax):
	if allpoints[(xmin,y)] in input:
		blacklist.add(allpoints[(xmin,y)])
	if allpoints[(xmax,y)] in input:
		blacklist.add(allpoints[(xmax,y)])
newinput = set(input) - set(blacklist)
input=newinput



print(max([list(allpoints.values()).count(x) for x in input]))

