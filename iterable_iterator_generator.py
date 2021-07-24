class MyIterable:
	def __init__(self, values):
		self.values = values

	def __iter__(self):
		return MyIterator(self.values)

class MyIterator:
	def __init__(self, values):
		self.values = values
		self.index = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.index >= len(self.values):
			raise StopIteration
			
		val = self.values[self.index]
		self.index +=1

		return val

values = [0, 1, 2, 3, 4]

iterableList = MyIterable(values)

#List comprehensions, for loops, and any iterating functions call iter() on our Iterable object
for val in iterableList:
	print(val)

print()

# We can do the same by hand
# The benefit is that we can then iterate over these iterators (which are consumed) without altering our iterable
iterator1 = iter(iterableList)
iterator2 = iter(iterableList)

# Iterate by hand
while True:
	try:
		print(next(iterator1))		# Next returns the next iterator item
	except StopIteration:
		print('End of iteration')
		break

print()

# Checking if an object is iterable
hasattr(object, '__iter__')


# GENERATOR
def myGenerator(values):
	for v in values:
		yield v

generator = myGenerator(values)
[print(v) for v in generator]

# A comprehension within parentheses is also a generator
generator = (v for v in values)
[print(v) for v in generator]

print(type(generator))