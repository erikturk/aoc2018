players = 418
turns = 71339*100

from collections import deque
scores = {x:0 for x in range(1,players+1)}
board=deque([0])
turn = 1
player =1
current = 1

while turn <= turns:
	if turn%23 ==0:
		board.rotate(7) 
		scores[player] += (turn +board.pop())
		board.rotate(-1)
	else:	
		board.rotate(-1)
		board.append(turn)

	turn += 1
	player +=1
	if player > players:
		player = 1

winner = max(scores,key=lambda key: scores[key])
print(winner,scores[winner])
