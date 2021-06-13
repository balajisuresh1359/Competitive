import time
import random 
class slidingPuzzle:
	def __init__(self,shape):
		self.matrix = []
		self.dictionary={}
		self.length = shape 
		self.load()
	def load(self):
		count=0
		temp=[]
		shape=self.length*self.length
		array=[x for x in range(1,shape)]
		shape=shape-1
		while count < self.length:
			newElement = random.randint(1,shape)
			if newElement in array:
				del array[array.index(newElement)]
				temp.append(newElement)
				if len(temp) == self.length :
					self.matrix.append(temp)
					temp=[]
					count+=1
				if len(temp) == self.length-1 and count == self.length-1:
					temp.append(" ")
					self.matrix.append(temp)
					count+=1
					temp=[]
		a=random.randint(0,self.length-1)
		b=random.randint(0,self.length-1)
		self.matrix[a][b] , self.matrix[self.length-1][self.length-1] = self.matrix[self.length-1][self.length-1],self.matrix[a][b] 
		for row in range(self.length):
			for column in range(self.length):
				self.dictionary[self.matrix[row][column]] = (row,column)

	def check(self):
		count=1
		empty=" "
		x,y=self.dictionary[empty]
		self.matrix[x][y] = 0
		for i in range(self.length):
			for j in range(self.length):
				if self.matrix[i][j] != count :
					self.matrix[x][y] = empty
					return False
				count+=1
				if count == self.length*self.length-1:
					self.matrix[x][y] = empty
					return True					
		self.matrix[x][y] = empty
		return True

	def startGame(self):
		step_No = 0
		while True:
			empty=" "
			for i in self.matrix:
				for j in i:
					print(" ",j," ",end=" ")
				print("\n")
			print("Move :  ",end=" ")
			start=time.time()
			try :
				element=int(input())
			except : 
				print("Wrong input.....\n")
				exitChoice = input("Do you want to exit.....?")
				if exitChoice == "stop" or exitChoice == "yes" or exitChoice == "yeah" or exitChoice == "0" :
					print("Bye...")
					return 0
				continue
			end=(time.time()-start)
			if element not in self.dictionary:
				continue
			x,y   = self.dictionary[element]
			x1,y1 = self.dictionary[empty]
			if ((x == x1) and (y == y1+1 or y == y1-1) ) or ((y == y1) and (x == x1+1 or x == x1-1)) :
				self.dictionary[empty]=(x,y)
				self.dictionary[element] = (x1,y1)
				self.matrix[x][y] = empty
				self.matrix[x1][y1] =element
			step_No+=1
			print("\nStep-Number : ",step_No,end=" ")
			print("  - Time taken : {:.2f} secs \n".format(end))
			if self.matrix[0][0] == 1 and self.matrix[self.length-1][self.length-1] == " ":
				if self.check():
					for i in self.matrix:
						for j in i:
							print(" ",j," ",end=" ")
						print("\n")
					return 1

level = int(input("Difficulty level  :  "))
if level >= 2: 
	puzzle=slidingPuzzle(level)
	start=time.time()
	result=puzzle.startGame()
	end=(time.time()-start)
	if result:
		print("\nYou won\n")
		print("Total time taken : {:.2f} secs \n".format(end))
