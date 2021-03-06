import numpy as np
import math

serial=1955
answer = (90,269,16)
SIZE=300

grid =np.ones((SIZE,SIZE),dtype=np.int64)
psize =np.zeros((SIZE,SIZE),dtype=np.int64)
pindex =np.zeros((SIZE,SIZE),dtype=np.int64)
psquares =np.zeros((SIZE,SIZE,SIZE),dtype=np.int64)
#size = np.zero((SIZE),dtype=np.int64)
for y in range(0,SIZE):
	for x in range(0,SIZE):
		d,i = math.modf((((x+11)*(y+1)+serial)*(x+11))/100)
		grid[x,y] = (int(i)%10)-5
		
for y in range(0,SIZE-2):
	for x in range(0,SIZE-2):
		size=dict()
		for s in range(3,30):
			if y+s > SIZE or x+s > SIZE:
				continue
			squaresum = sum(grid[x:x + s + 1, y:y + s + 1].ravel())
			psquares[x, y, s] = squaresum
		



print(np.amax(psquares))
print(np.argmax(psquares))
print(np.unravel_index(np.argmax(psquares),psquares.shape))

print('for serial 18 ans should be 90,269,16')
print('for serial 42 ans should be 232,251,12')
