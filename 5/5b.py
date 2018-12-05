file=open("input","r")
source= file.readlines()
file.close()

letters= "abcdefghijklmnopqrstuvwxyz"

for l in list(letters):
	translation = str.maketrans("","",l+str.upper(l))

	input = source[0].translate(translation)
	i = 1
	start=input[0]
	end=""
	while (i <= (len(input)-2)):
		#print(i,start,input[i])
		if str.lower(input[i]) == str.lower(start[-1]):
			if str.islower(start[-1]) and str.isupper(input[i]):
				#print(start[-1],input[i+1])
				if len(start) == 1:
					start = input[i+1]
					i+=2
				else:
					start = start[:-1]
					i+=1
		
			elif str.isupper(start[-1]) and str.islower(input[i]):
				#print(start[-1],input[i+1])
				if len(start) == 1:
					start = input[i+1]
					i+=2
				else:
					start = start[:-1]
					i+=1
			else:
				start = start + input[i]
				i+=1
		else:
			start= start + input[i]	
			i+=1

	print(l,len(start))
