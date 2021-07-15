import unittest

class Person():
	def __init__(self, firstName, lastName):
		self.firstName = firstName
		self.lastName = lastName

	def fullName(self):
		return ' '.join([self.firstName, self.lastName])

class TestPerson(unittest.TestCase):
	#Executed before each test
	def setUp(self):
		self.person = Person('John', 'Doe')

	#Executed after each test
	def tearDown(self):
		pass

	def test_fullName(self):
		self.assertEqual(self.person.fullName(), 'John Doe')

		self.person.firstName = 'Bob'
		self.assertEqual(self.person.fullName(), 'Bob Doe')

#Calling this will run all test methods
unittest.main()