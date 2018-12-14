from pprint import pprint
file=open("testinput","r")
source = file.readlines()
file.close()

gen=list()
rules = list()
gen.append(source[0].split(" ")[2].rstrip())

for i in range(2,len(source)):
	rules.append( source[i].rstrip())

potdict=dict()
pprint(rules)
print(gen)

gen[0] = gen[0]
print(gen)
thisgen = gen[0]
newstart = -2

def tester(testpot):
	for rule in rules:
		condition = rule.split(' ')[0]
		result = rule.split(' ')[2]
		if condition == testpot:
			return result
	return '.'

def printgen(potdict,start=0):
	for i in range(min(min(list(potdict.keys())),start),max(potdict.keys())+3):
		if i in potdict:
			print(potdict[i],end='')
		else:
			print('.',end="")
	print()
	return
		
### fill a dict with location:status

for i,v in enumerate(list(source[0].split(" ")[2].rstrip())):
	potdict[i]=v
potdictgen = list()
print('start potdict is:')
printgen(potdict)
potdictgen.append(potdict)



while len(potdictgen) <= 20:
	print('generation is: ',len(potdictgen)-1)
	printgen(potdict)

	startpotdict =min(potdict.keys()) # for this potdict, this is the start
	nextpotdict = dict()
	# let's check the 4 pots to the left of the start
	addpots = 4
	for i in range(startpotdict-4,startpotdict):
		testpot = ('.' * addpots)
		for j in range (0,5-addpots):
			testpot = testpot + potdict[j]
		if tester(testpot) == '#':
			nextpotdict[i+2]=tester(testpot)
		addpots -= 1


	print(nextpotdict)
	
	nextgen = ""

	
	
	for i in range(min(potdict.keys()),max(potdict.keys())+4):
		testpot=""
		for j in range(i-2,i+3):
			if j in potdict:
				testpot = testpot + potdict[j]
			else:
				testpot = testpot + '.'
		nextpotdict[i]=tester(testpot)

	printgen(nextpotdict)
	if nextpotdict[min(list(nextpotdict.keys()))] == '.' and min(list(nextpotdict.keys())) < 0:
		print('foundone')
		print(min(list(nextpotdict.keys())))
		print(nextpotdict[min(list(nextpotdict.keys()))])
		
		del nextpotdict[min(list(nextpotdict.keys()))]
	potdictgen.append(nextpotdict)
	potdict = potdictgen[-1]
	printgen(potdict)
	nextpotdict = dict()


for i,v  in enumerate(potdictgen):
	print('%2d:' % i,end="")
	printgen(v,-3)
total = 0
for i in potdictgen[-1]:
	if potdictgen[-1][i]=='#':
		total += i
print(total)
