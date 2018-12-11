import parse
from parse import compile

class Dot:
	def __init__(self,firstdict):
		
		self.px = firstdict['px']
		self.py = firstdict['py']
		self.vx = firstdict['vx']
		self.vy = firstdict['vy']

	def next(self):
		self.px += self.vx
		self.py += self.vy

	def willbe(self):
		return (self.px + self.vx,self.py + self.vy)

	def __repr__(self):
		return "{},{}".format(self.px,self.py)

	def x(self):
		return int(self.px)

	def y(self):
		return int(self.py)

def max_x():
	return max([dots[x].x() for x in dots.keys()])

def min_x():
	return min([dots[x].x() for x in dots])

def max_y():
	return max([dots[x].y() for x in dots])

def min_y():
	return min([dots[x].y() for x in dots])

def move():
	for i in dots.keys():
		dots[i].next()
	return

def x_on_line(y):
	return sorted(set([ dots[i].x() for i in dots if dots[i].y() == y]))



def draw():
	start = min_x()
	width = abs(max_x())+abs(min_x())+1
	for i in range(min_y(),max_y()+1):
		last = start
		total = 0
		for j in x_on_line(i):
			print(("." *abs(last - j))+"X",end="")
			total += abs(last -j)+1
			last = j+1
		
		
		if total < width:
			print("."*abs(width - total))
		else:
			print()
	print("\n\n")		
from copy import deepcopy
file = open("input","r")
source = file.readlines()
file.close()

p = compile("position=<{px:d}, {py:d}> velocity=<{vx:d}, {vy:d}>")
parsed = p.parse(source[0])
print(parsed)
dots = {}
for i,v in enumerate(source):
	dots[i] = Dot(p.parse(v).named)

print(max_x(),max_y(),min_x(),min_y())
t=1
while True:
	spacing  = max_y() - min_y()
	future_y = [dots[x].willbe()[1] for x in dots]
	if spacing <= (max(future_y) - min(future_y)):
		print(spacing,(max(future_y) - min(future_y)))
		draw()
		print(t)
		break
	move()
	t+=1

