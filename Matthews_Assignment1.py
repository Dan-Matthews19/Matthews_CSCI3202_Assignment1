#Dan Matthews, CSCI 3202 Assignment 1
#GitHub username: Dan-Matthews19

import Queue

#queue implementation
q = Queue.Queue()


#stack implementation
class myStack():
	def __init__(self):
		self.container = []

	def push(self, number):
		self.container.append(number)

	def pop(self):
		return self.container.pop()

	def checkSize(self):
		return len(self.container)

#binary tree implemenation
class Node():
	def __init__(self, value,parent):
		self.value = value
		self.left = None
		self.right = None
		self.parent = parent

class BinaryTree():
	def __init__(self):
		self.root = None

	def createRoot(self, value):
		if self.root == None:
			self.root = Node(value,None)
		return self.root
	
	def add(self, value, parentValue):
		root = self.root
		if root == None:
			root = Node(value)
		parent = self.searchTree(parentValue)
		if parent is not None:
			if parent.left is None and parent.right is None:
				parent.left = Node(value,parent)
			elif parent.left is not None and parent.right is None:
				parent.right = Node(value,parent)
			elif parent.left is not None and parent.right is not None:
				print "parent has two children, node not added"
		else:
			print "parent not found"

	def delete(self, value):
		nodeToDelete = self.searchTree(value)
		if nodeToDelete:
			if nodeToDelete.left != None:
				if nodeToDelete.right!= None:
					print "Node not deleted, has children"
			else:
				if nodeToDelete.parent.left == nodeToDelete:
					nodeToDelete.parent.left = None
					del nodeToDelete
				elif nodeToDelete.parent.right == nodeToDelete:
					nodeToDelete.parent.right = None
					del nodeToDelete
		else:
			return "node not found"		


	def searchTree(self, value):
		searchQueue = Queue.Queue()

		curNode = self.root
		while(isinstance(curNode, Node)):
			if curNode.value == value:
				return curNode
			else:
				searchQueue.put(curNode.left)
				searchQueue.put(curNode.right)
				curNode = searchQueue.get()
		return None

	def preorderPrint(self, node):
		if node is not None:
			print node.value
			self.preorderPrint(node.left)
			self.preorderPrint(node.right)


class Graph():
	def __init__(self,graphData={}):
		self.graphData = graphData

	def addVertex(self, node):
		if node in self.graphData:
			print "vertex already exists"
		else:
			self.graphData[node] = []

	def addEdge(self, node1, node2):
		if node1 not in self.graphData or node2 not in self.graphData:
			print "verticies not found!"
		else:
			self.graphData[node1].append(node2)
			self.graphData[node2].append(node1)

	def findVertex(self,value):
		if value in self.graphData:
			print value, ":", self.graphData[value]
		else:
			print "vertex not found"



def main():
	print "***Queue testing:***"
	for i in range(10):
		q.put(i)

	while not q.empty():
		print q.get()
	
	print "***Stack testing:***"
	s = myStack()
	s.push(1)
	s.push(2)
	s.push(3)
	s.push(4)
	s.push(5)
	s.push(6)
	s.push(7)
	s.push(8)
	s.push(9)
	s.push(10)
	first = s.pop()
	print first
	second = s.pop()
	print second
	third = s.pop()
	print third
	fourth = s.pop()
	print fourth
	fifth = s.pop()
	print fifth
	sixth =  s.pop()
	print sixth
	seventh = s.pop()
	print seventh
	eighth = s.pop()
	print eighth
	ninth = s.pop()
	print ninth
	tenth = s.pop()
	print tenth

	print "***Testing the tree***"
	print "adding nodes"
	tree = BinaryTree()
	tree.createRoot(8)
	tree.add(7,8)
	tree.add(9,8)
	tree.add(6,7)
	tree.add(10,7)
	tree.add(5,6)
	tree.add(4,9)
	tree.add(11,9)
	tree.add(3,11)
	tree.add(12,11)

	tree.preorderPrint(tree.root)
	
	print "deleting nodes"
	tree.delete(12)
	tree.delete(5)
	tree.preorderPrint(tree.root)
	
	print "***Testing Graph***"
	
	graph = Graph()

	graph.addVertex(1)
	graph.addVertex(2)
	graph.addVertex(3)
	graph.addVertex(4)
	graph.addVertex(5)
	graph.addVertex(6)
	graph.addVertex(7)
	graph.addVertex(8)
	graph.addVertex(9)
	graph.addVertex(10)
	
	graph.addEdge(1,2)
	graph.addEdge(2,3)
	graph.addEdge(3,4)
	graph.addEdge(4,5)
	graph.addEdge(5,6)
	graph.addEdge(6,7)
	graph.addEdge(7,8)
	graph.addEdge(8,9)
	graph.addEdge(9,10)
	graph.addEdge(1,3)
	graph.addEdge(2,4)
	graph.addEdge(3,5)
	graph.addEdge(4,6)
	graph.addEdge(5,7)
	graph.addEdge(6,8)
	graph.addEdge(7,9)
	graph.addEdge(8,10)
	graph.addEdge(10,2)
	graph.addEdge(2,6)
	graph.addEdge(5,8)
	
	print "search for vertices 3,6,7,8,10"
	graph.findVertex(3)
	graph.findVertex(6)
	graph.findVertex(7)
	graph.findVertex(8)
	graph.findVertex(10)
	
	
	


main()
