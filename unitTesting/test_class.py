import unittest
from unittesting import sampleClass

class TestPerson(unittest.TestCase):
	#Ran when the CLASS is created (not instanced)
	@classmethod
	def setUpClass(cls):
		pass

	#Runs when class is tore down (not instances)
	@classmethod
	def tearDownClass(cls):
		pass

	#Executed before each test
	def setUp(self):
		self.person = unitTesting.sampleClass.Person('John', 'Doe')

	#Executed after each test
	def tearDown(self):
		pass

	def test_fullName(self):
		self.assertEqual(self.person.fullName(), 'John Doe')

		self.person.firstName = 'Bob'
		self.assertEqual(self.person.fullName(), 'Bob Doe')

#Calling this will run all test methods
#Using this syntax ensures the code is run only when running the class, not when importing the module
if __name__ == '__main__':
	unittest.main()