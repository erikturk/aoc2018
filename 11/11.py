import numpy as np
import math

serial=71

grid =np.ones((300,300),dtype=np.int64)
print(grid)

for y in range(0,300):
	for x in range(0,300):
		d,i = math.modf((((x+11)*(y+1)+serial)*(x+11))/100)
		grid[x,y] = (int(i)%10)-5
		

print(grid[100,152])		
