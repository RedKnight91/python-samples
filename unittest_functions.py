import unittest
from unittesting import sample_functions
	
class TestFunctions(unittest.TestCase):
	#Tests MUST start with 'test_', otherwise they won't be run
	def test_multiply(self):
		result = sample_functions.multiply(3, 9)

		#Use .assert... methods to verify function outcomes
		self.assertEqual(result, 27)

	def test_divide(self):
		result = sample_functions.divide(6, 3)
		self.assertEqual(result, 2)

		#Context manager used to catch exceptions
		with self.assertRaises(ValueError):
			sample_functions.divide(6, 0)

#Calling this will run all test methods
#Using this syntax ensures the code is run only when running the class, not when importing the module
if __name__ == '__main__':
	unittest.main()