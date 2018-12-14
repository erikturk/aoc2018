from pprint import pprint
file=open("testinput","r")
source = file.readlines()
file.close()

gen=list()
rules = list()
gen.append(source[0].split(" ")[2].rstrip())

for i in range(2,len(source)):
	rules.append( source[i].rstrip())

pprint(rules)
print(gen)

thisgen = gen[0]+'....'
newstart = -2
while len(gen) <= 20:
	
	nextgen = ""
	for pot in range(len(thisgen)):
		testpot = thisgen[pot:pot+5]
		answer = 'X'
		for rule in rules:
			condition = rule.split(' ')[0]
			result = rule.split(' ')[2]
			if condition == testpot:
				answer = result
		if answer == 'X':
			answer = '.'
		nextgen = nextgen+answer
	gen.append(nextgen)	
	thisgen = '..'+''.join(gen[-1])+'..'
	newstart += -1
for i,v  in enumerate(gen):
	print('%2d:' % i,v)
total = 0
for i in range(newstart,len(gen[-1])):
	if gen[-1][i] == '#':
		total += i

print(total)
