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

		previous.next = node.next
		node.next = None
		node.prev = None

		self.length -= 1

		return node

linked = LinkedList()
assert(linked.head == None)
assert(linked.length == 0)
assert(linked.tail == None)
empty_list = linked.search('thing')
assert(empty_list == 'This is an empty list')

linked.append('first')
assert(linked.head.data == 'first')
assert(linked.tail.data == 'first')
assert(linked.length == 1)

linked.append('second')
assert(linked.head.data == 'first')
assert(linked.head.next.data == 'second')
assert(linked.tail.data == 'second')
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

linked.append('third')
assert(linked.length == 3)
mid = linked.remove_middle('second')
assert(linked.length == 2)
assert(linked.head.next.data == 'third')

print('passed!')
