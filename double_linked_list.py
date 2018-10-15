class Node(object):

	def __init__(self, data):

		self.data = data
		self.next = None
		self.prev = None

	def __repr__(self):
		return "<Node: {}>".format(self.data)

test = Node('test')
assert(test.data=='test')
assert(test.next == None)


class LinkedList():

	def __init__(self):
		
		self.head = None
		self.tail = None
		self.length = 0


	def append(self, data):
		new_node = Node(data)
		self.length += 1
		if self.head == None:
			self.head = new_node
			self.tail = new_node

		#find the tail, set the tail's .next to be new_node
		else:
			tail = self.tail
			new_node.prev = tail
			tail.next = new_node
			self.tail = new_node

		return new_node


	def search(self, search):

		if self.head == None:
			return 'This is an empty list'

		current = self.head
		found = False

		while not found:
			if current.data == search:
				found = True
			elif current.next == None:
				return 'not in list'
			else:
				current = current.next

		return current

	def remove_last(self):

		tail = self.tail
		soon_tail = tail.prev

		tail.prev = None
		soon_tail.next = None
		self.tail = soon_tail

		self.length -= 1

		return tail


	def remove_middle(self, data):
		
		node = self.search(data)

		previous = node.prev
		previous = node.next
		node.next = None
		node.prev = None

		self.length -= 1

		return node