multiply = lambda numA, numB: numA * numB

def divide(numA, numB):
	if numB == 0:
		raise ValueError('Division by zero')

	return numA / numB