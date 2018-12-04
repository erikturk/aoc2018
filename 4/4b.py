file = open("input","r")
input = file.readlines()
file.close()

sleeptime=dict()
totalsleeptime=dict()
guard=0
for i in sorted(input):
	date = i.split(']')[0].split(" ")[0].lstrip('[')
	time = i.split(']')[0].split(" ")[1].lstrip('[')
	if '#' in i.split(']')[1]:
		newguard =int(i.split(']')[1].split('#')[1].split(' ')[0])
		if newguard != guard:
			guard = newguard

	if guard not in sleeptime:
		sleeptime[guard] = dict()
	if guard not in totalsleeptime:
		totalsleeptime[guard] = 0
	
	if 'falls asleep' in i.split(']')[1]:
		startsleep = int(time.split(':')[1])


	if 'wakes up' in i.split(']')[1]:
		stopsleep= int(time.split(':')[1])
		totalsleeptime[guard] += (stopsleep - startsleep)
		for min in range(startsleep,stopsleep):
			if min in sleeptime[guard]:
				sleeptime[guard][min] += 1
			else:
				sleeptime[guard][min] = 1

maxsleep = dict()
maxtimes =0
for guard in sleeptime.keys():
	if sleeptime[guard]:
		
		maxsleep[guard] = max(sleeptime[guard],key=sleeptime[guard].get)
		print(guard,maxsleep[guard],sleeptime[guard][maxsleep[guard]],guard*maxsleep[guard])


