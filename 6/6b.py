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
		pointtotal=0
		for p in input:
			pointtotal += abs(x-p[0])+abs(y-p[1])
		if pointtotal <= 10000:
			allpoints[(x,y)] = 1
		else:
			allpoints[(x,y)] = 0


print(list(allpoints.values()).count(1))

