import numpy as np
import math

serial=1955
SIZE=300

grid =np.ones((SIZE,SIZE),dtype=np.int64)
plevel =np.zeros((SIZE,SIZE),dtype=np.int64)
#size = np.zero((SIZE),dtype=np.int64)
for y in range(0,SIZE):
	for x in range(0,SIZE):
		d,i = math.modf((((x+11)*(y+1)+serial)*(x+11))/100)
		grid[x,y] = (int(i)%10)-5
		
for y in range(0,SIZE-2):
	for x in range(0,SIZE-2):
			plevel[x,y]=sum(grid[x:x+3,y:y+3].ravel())
		

print(grid)

print(np.amax(plevel))
x,y = np.unravel_index(np.argmax(plevel),plevel.shape)
print(x+1,y+1)
