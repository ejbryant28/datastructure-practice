class Node(object):

	def __init__(self, data):

		self.data = data
		self.next = None

	def __repr__(self):
		return "<Node: {}>".format(self.data)

test = Node('test')
assert(test.data=='test')
assert(test.next == None)


class LinkedList():

	def __init__(self):
		
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


	def append(self, data):
		new_node = Node(data)
		self.length += 1
		if self.head == None:
			self.head = new_node
			return 'completed'

		#find the tail, set the tail's .next to be new_node
		tail = self._find_tail()
		tail.next = new_node
		return 'completed'
		

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

		pen_ultimate = self._find_penultimate()

		tail = pen_ultimate.next
		pen_ultimate.next = None

		self.length -= 1

		return tail
		

	def remove_middle(self, data):
		
		prev = self._find_penultimate(data)
		search = prev.next

		prev.next = search.next
		search.next = None

		return search

linked = LinkedList()
assert(linked.head == None)
assert(linked.length == 0)
empty_list = linked.search('thing')
assert(empty_list == 'This is an empty list')

linked.append('first')
assert(linked.head.data == 'first')
assert(linked.length == 1)

linked.append('second')
assert(linked.head.data == 'first')
assert(linked.head.next.data == 'second')
assert(linked.length == 2)


not_found = linked.search('third')
assert(not_found == 'not in list')

search = linked.search('first')
assert(search.data == 'first')

linked.append('third')
assert(linked.length == 3)
last = linked.remove_last()
assert(last.data == 'third')
assert(linked.length == 2)

print('passed!')
