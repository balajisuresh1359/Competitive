def generatePrime(limit):
	primeNum=[2,3]
	flag=0
	for i in range(3,limit+1,2):    
		for j in primeNum:		
			if i%j == 0:			
				flag=0			
				break
		if flag :					
			primeNum.append(i)		
		flag =1
	return primeNum

print(generatePrime(16))
