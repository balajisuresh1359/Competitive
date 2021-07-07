class BinaraySearchTree():

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def addNode(self,node):
		if node == self.data :
			return print("Duplicate element...")
		if self.data < node:
			if self.right:
				self.right.addNode(node)
			else:
				self.right = BinaraySearchTree(node)
		else:
			if self.left:
				self.left.addNode(node)
			else:
				self.left = BinaraySearchTree(node)


	def inorder(self):
		if self:
			if self.left:
				self.left.inorder()
			print(self.data,end="  ")
			if self.right:
				self.right.inorder()

	def search(self,element):
		if self.data == element:
			return self
		elif self.data < element :
			if self.right:
				return self.right.search(element)
		else:
			if self.left:
				return self.left.search(element)
		return False


	def checkTree(self,root1,root2):
		if root2 == None and root1 == None:
			return True
		l=not(root2.left !=None and  root1.left==None)
		r=not(root2.right !=None and root1.right == None)
		if l:
			if root2.left != None and root1.left != None: 
				l = self.checkTree(root1.left,root2.left)
		if r:
			if root2.right != None and root1.right != None: 
					r = self.checkTree(root1.right,root2.right)
		return (root1.data == root2.data and l and r)


	def issubtree(self,subrootptr):
		branchroot  = self.search(subrootptr.data)
		if branchroot:
			return self.checkTree(branchroot,subrootptr)
		return False


#--------------------------------------------------------------------------------------------------------------------

if __name__=="__main__":
	root = BinaraySearchTree(15)
	root.addNode(12)
	root.addNode(20)
	root.addNode(9)
	root.addNode(13)
	root.addNode(10)
	root.addNode(17)
	root.addNode(24)
	root.addNode(16)
	root.addNode(19)
	root.addNode(25)
	root.addNode(30)
	root.addNode(31)
	root.addNode(18)
	root.inorder()
	print("\n")
	subroot =BinaraySearchTree(15)
	subroot.addNode(20)
	subroot.addNode(12)
	subroot.addNode(13)
	subroot.inorder()
	print("\n")
	print(root.issubtree(subroot))

