class Node:
	def __init__(self, x):
		self.value = x
		self.left = None
		self.right = None
		self.h = 1
 
class TreeSet:
	def __init__(self):
		self.root = None
		self.nodes = set()
 
	def add(self, x): 
		self.nodes.add(x)
		self.insert(self.root, x)
		
	def insert(self, root, x):
		if not root:
			return Node(x)
		elif root.value > x:
			root.left = self.insert(root.left, x)
		else:
			root.right = self.insert(root.right, x)
		
		root.h = 1+max(self.height(self.root.left), self.height(self.root.right))
 
		b = self.balance(root)
			
		if b > 1 and x < root.left.value:
			return self.rRotate(root)
		
		if b < -1 and x > root.right.value:
			return self.lRotate(root)
		
		if b > 1 and x > root.left.value:
			root.left = self.lRotate(root.left)
			return self.rRtotate(self.root)
		
		if b < -1 and x < root.right.value:
			self.root.right = self.rRotate(root.right)
			return self.lRotate(root)
		return root
	
	def lRotate(self, node):
 
		r = node.right
		l = node.left
 
		r.left = node
		node.right = l
 
		node.h = 1 + max(self.height(node.left), self.height(node.right))
		r.h = 1 + max(self.height(r.left), self.height(r.right))
 
		return r
	
	def rRotate(self, node):
 
		l = node.left
		r = node.right
 
		l.right = node
		node.left = r
 
		node.h = 1+max(self.height(node.left), self.height(node.right))
		l.h = 1+max(self.height(l.left), self.height(l.right))
 
		return l
	
	def height(self, node):
		if not node:
			return 0
		return node.h
		
	def balance(self, node):
		if not node:
			return 0
		return self.height(node.left) - self.height(node.right)
		
	def __contains__(self, x):
		if x in self.nodes:
			return True
		if not self.root:
			return False
		
		return False
 
	def __repr__(self):
		items = list(sorted(self.nodes))
		return str(items)
 
 
if __name__ == "__main__":
	s = TreeSet()
	s.add(1)
	s.add(2)
	s.add(4)
	print(1 in s) # True
	print(2 in s) # True
	print(3 in s) # False
	print(4 in s) # True
	print(s) # [1, 2, 4]