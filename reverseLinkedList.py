class Node:
	"""docstring for Node"""
	def __init__(self, data,next=None):
		self.data = data
		self.next=next

class LinkedList:
	def __init__(self):
		self.head=None

	def reverseList(self):
		#1 2 3 4 5 None
		#5 4 3 2 1 None
		previous = None
		current =self.head
		while current: 					# 1 | 2 | 3 | 4 | 5 | None
			nextptr = current.next 		# 2 | 3 | 4 | 5 | None
			current.next =previous 		# None | 1 | 2 | 3 | 4 
			previous = current 			# 1 | 2 | 3 | 4 | 5
			current = nextptr			# 2 | 3 | 4 | 5 | None
		self.head = previous			# 5

	def appendNode(self,data):
		new_node=Node(data)
		if not self.head:
			new_node.next = self.head
			self.head=new_node
		else:
			ptr = self.head
			while ptr.next:
				ptr =ptr.next
			ptr.next = new_node
	
	def show(self):
		ptr=self.head  
		while ptr:
			print(ptr.data,end="   ")
			ptr=ptr.next
		print("\n")

if __name__ == "__main__":
	root = LinkedList()
	root.appendNode(1)
	root.appendNode(2)
	root.appendNode(3)
	root.appendNode(4)
	root.appendNode(5)
	root.show()
	root.reverseList()
	root.show()


		