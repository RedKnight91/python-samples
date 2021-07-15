import unittest

multiply = lambda numA, numB: numA * numB

def divide(numA, numB):
	if numB == 0:
		raise ValueError('Division by zero')

	return numA / numB
	
class TestFunctions(unittest.TestCase):

	#Tests MUST start with 'test_', otherwise they won't be ran
	def test_multiply(self):
		result = multiply(3, 9)

		#Use .assert... methods to verify function outcomes
		self.assertEqual(result, 27)

	def test_divide(self):
		result = divide(6, 3)
		self.assertEqual(result, 2)

		#Context manager used to catch exceptions
		with self.assertRaises(ValueError):
			divide(6, 0)

#Calling this will run all test methods
unittest.main()