class MyIterable:
	def __init__(self, values):
		self.values = values

	def __iter__(self):
		return MyIterator(self.values)

class MyIterator:
	index = 0

	def __init__(self, values):
		self.values = values

	def __iter__(self):
		return self

	def __next__(self):
		if self.index >= len(self.values):
			raise StopIteration
			
		val = self.values[self.index]
		self.index +=1

		return val

iterableList = MyIterable([0, 1, 2, 3, 4])

#List comprehensions, for loops, and any iterating functions call iter() on our Iterable object
for val in iterableList:
	pass

# We can do the same by hand
# The benefit is that we can then iterate over these iterators (which are consumed) without altering our iterable
iterator1 = iter(iterableList)
iterator2 = iter(iterableList)

# Iterate by hand
while True:
	try:
		val = next(iterator1)
	except StopIteration:
		print('End of iteration')
		break