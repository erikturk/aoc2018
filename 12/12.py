from pprint import pprint
file=open("testinput","r")
source = file.readlines()
file.close()

gen=list()
rule = list()
gen.append(source[0].split(" ")[2].rstrip())

for i in range(2,len(source)):
	rule.append( source[i])












print(gen)

pprint(rule)
