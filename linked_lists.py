class Node(object):

	def __init__(self, data):

		self.data = data
		self.next = None

	def __repr__(self):
		return "<Node: {}>".format(self.node)

class LinkedList(Node):

	def __init(self):
		
		self.head = None
		self.length = 0

	def _find_tail(self):

		tail = False
		current = self.head

		while not tail:
			if current.next == None:
				tail = current

			else: 
				current = current.next

		return tail

	def _find_penultimate(self, search=None):

		penult = None
		current = self.head

		while not penult:
			if current.next.next == search:
				penult = current

			else:
				current = current.next
		return penult


	def append(self, data)
		new_node = Node(data)
		self.length += 1
		if self.head == None:
			self.head = new_node
			return 'completed'

		#find the tail, set the tail's .next to be new_node
		tail = _find_tail()
		tail.next = new_node
		return 'completed'
		

	def search(self, data):

		if self.head == None:
			return 'This is an empty list'

		current = self.head
		found = False

		while not found:
			if current.data == data:
				found = True
			elif current.next == None:
				return 'not in list'
			current = current.next

		return current

	def remove_last(self):

		pen_ultimate = _find_penultimate()

		tail = pen_ultimate.next
		pen_ultimate.next = None

		self.length -= 1

		return tail
		

	def remove_middle(self, data):
		
		prev = _find_penultimate(data)
		search = prev.next

		prev.next = search.next
		search.next = None

		return search