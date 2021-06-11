import time
def rotateArray(array,i,size,direction):
	size=size-1	
	if direction: #rotate left to right
		while i!=0:  #iteration variable
			lastElement = array[size] #store the last element in a variable
			j=size-1	
			while j!=-1: #till all elements shifted to right except the last one
				array[j+1]=array[j]
				j-=1
			array[0]=lastElement #store last element in the first position
			i-=1
	else:         #rotate right to left
		while i!=0:	#iteration variable
			firstElement = array[0]   #store the first element in a variable
			j=0
			while j!=size: #till all elements shifted to left except the first one
				array[j]=array[j+1]
				j+=1
			array[size] = firstElement  ##store first element in the last position
			i-=1
	return array


def rotateColumn(matrix,column,i,size,direction):
	size=size-1
	if direction:  #rotate top to bottom
		while i!=0: #iteration variable
			j=size-1 
			lastElement = matrix[size][column] #store  value of the last element in column number "column"
			while j!=-1:  #till all elements in column number "column" shifted to one position down
				matrix[j+1][column] = matrix[j][column]
				j-=1
			matrix[0][column] =lastElement  #store the last element in column number "column" in the first postion 
			i-=1
	else:
		while i!=0:
			j=0
			firstElement=matrix[0][column] #store  value of the first element in column number "column"
			while j!=size:
				matrix[j][column] = matrix[j+1][column] #till all elements in column number "column" shifted to one position up
				j+=1
			matrix[size][column]=firstElement #store the first element in column number "column" in the last postion 
			i-=1
	return matrix

def matrixRotation(matrix,row,column,i,size,direction):
	if column :  #rotate column
		matrix=rotateColumn(matrix,column,i,size,direction)
	else: #rotate row
		matrix[row] = rotateArray(matrix[row],i,size,direction)

	for i in matrix:
		for j in i:
			print(j,end="  ")
		print("\n")

def startRotate():
	print("Direction                       |         Code")
	time.sleep(1)
	print("----------------------------------------------")
	time.sleep(1)
	print("rigth to left / bottom to top   |          0  ")	
	time.sleep(1)
	print("left to rigth / top to bottom   |          1  ")	
	time.sleep(1)
	print("----------------------------------------------\n")
	print("Input format  : [row/column] [row/column number] [number of iteration] [direction code]")	
	#row 1 2 0
	matrix=[[1,2,3],[4,5,6],[7,8,9]]
	size=len(matrix)
	while True :
		print("Enter : ",end=" ")
		want_to =input()
		parser=want_to.split(" ")
		if parser[0] == "row":
			matrixRotation(matrix,int(parser[1]),0,int(parser[2]),size,int(parser[3]))
		else:
			matrixRotation(matrix,0,int(parser[1]),int(parser[2]),size,int(parser[3]))



if __name__ == "__main__":
	startRotate()
