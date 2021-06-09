def longestPalindrome(string):
	reversedString=string[::-1]
	i=0
	start=0
	end=0
	postions=set()
	irev=1
	count=len(string)
	while count!=1:
		irev=i
		end=0
		j=0
		i+=1
		size=len(string)
		while irev < size:
			if string[j] == reversedString[irev]:
				start=j
				while irev<size and  string[j] == reversedString[irev]:
					end+=1
					j+=1
					irev+=1
				j-=1
				irev-=1
				if end > 1 :
					postions.add((start,end+start))
				end=0
				start=0
			j+=1
			irev+=1
		count-=1
	maxi=0
	temp=""
	for items in postions:
		x,y=items
		if string[x:y] == "".join(reversed(string[x:y])):
			if maxi < y-x:
				maxi=y-x
				temp=string[x:y]
	return temp


string="babcbabcbaccba"
print(longestPalindrome(string))
