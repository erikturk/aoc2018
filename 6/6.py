file = open("testinput","r")
source= file.readlines()
file.close()
input=list()
for i in source:
	input.append((int(i.split(",")[0]),int(i.split(",")[1])))
	

print(input)
dist2next = dict()
for i in input:
	print(i)
	for j in input:
		print( abs(i[0] - j[0]) + abs(i[1] - j[1]))
		dist2next[(i,j)] = abs(i[0]-j[0]) + abs(i[1] - j[1])

print(dist2next)
