players = 418
turns = 71339*100

scores = {x:0 for x in range(1,players+1)}
board=[0,1]
turn = 2
player =2
current = 1

print('[-] (0)')
print('[1] 0 (1)')
while turn <= turns:
	if turn%23 ==0:
		current = (current -7) % len(board) 
		scores[player] += (turn +board[current])
		board.remove(board[current])
	else:	
		board.insert((current+1)%(len(board))+1,turn)
		current= board.index(turn)
	turn += 1
	player +=1
	if player > players:
		player = 1

winner = max(scores,key=lambda key: scores[key])
print(winner,scores[winner])
