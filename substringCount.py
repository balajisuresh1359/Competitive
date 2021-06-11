
def subStringcount(string,substring):
	count=0
	match=0
	size=len(string)
	subsize=len(substring)
	for i in range(size):
		if string[i] != substring[match]:
			match=0
		else:
			match+=1
		if match == subsize:
			count+=1
			match=0
	return count




string="githubqwegithubrtyuigithubwertyugithubfgvjbkngithubi"
print(subStringcount(string,"github"))
