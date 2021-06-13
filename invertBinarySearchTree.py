class BinaryTree:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def addNode(self,data):

		if self.data == data :
			return 
		if self.data > data :
			if self.left :
				self.left.addNode(data)
			else:
				self.left = BinaryTree(data)

		else:
			if self.right:
				self.right.addNode(data)
			else:
				self.right=BinaryTree(data)

	def display(self,root):
		if root:
			self.display(root.left)
			self.display(root.right)
			print(root.data,end=" ")

	def invertTree(self,root):  #postorder traversal
		if root :
			self.invertTree(root.left)
			self.invertTree(root.right)
			root.left,root.right = root.right,root.left


if __name__ == "__main__":
	root =BinaryTree(4)
	root.addNode(3)
	root.addNode(5)
	root.addNode(2)
	root.addNode(1)
	root.addNode(8)
	root.display(root)
	print("\n")
	root.invertTree(root)
	root.display(root)
