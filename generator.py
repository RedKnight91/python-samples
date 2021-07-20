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
printSizeOf('Mem Size:', numbers, 'Previous numbers generator')
printSizeOf('Mem Size:', squaredNumbers, 'Square numbers generator')
printSizeOf('Mem Size:', numbersList, 'Generator converted to list')