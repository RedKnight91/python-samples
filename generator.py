def printSizeOf(obj, message):
	import sys
	
	size = sys.getsizeof(obj)
	print(size, message)

def prevNumbers(num):
	for i in range(0, num):
		yield i

def squareNumbers(numList):
	for n in numList:
		yield n*n

num = 10000

#This is a generator
numbers = prevNumbers(num)

#We can pass a generator to another generator
squaredNumbers = squareNumbers(numbers)

#Calling list() on a generator will convert it to a list
numbersList = list(numbers)

#The list() variables contain all of the values in memory and are much heavier
printSizeOf(numbers, 'Previous numbers generator')
printSizeOf(squaredNumbers, 'Square numbers generator')
printSizeOf(numbersList, 'Generator converted to list')


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

from dataclasses import dataclass
@dataclass
class Counter:
	code: str
	start: int
	end: int

	counter = 0

	def count(self):
		if self.inRange():
			self.counter += 1

	inRange = lambda self: self.counter < self.end

#Complex generator, creating and iterating objects
def counterCreator(codeStart, codeEnd, countStart, countEnd):
	for code in range(ord(codeStart), ord(codeEnd)):
		counter = Counter(chr(code), countStart, countEnd)

		while counter.inRange():
			counter.count()
			yield counter

counters = counterCreator('a', 'c', 1, 4)

[print(id(c), repr(c), c.counter) for c in counters]


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#Generator working with an iterator
def squareGenerator(values):
	iterator = iter(values)
	value = next(iterator)	#Necessary to start the iterator

	while True:
		square = value * value
		yield square		#Won't exit the block of code

		try:
			value = next(iterator)	#Used to stop iteration
		except StopIteration:
			break

values = [1, 2, 3]
[print('Square:', square) for square in squareGenerator(values)]