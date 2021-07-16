class Person():
	def __init__(self, firstName, lastName):
		self.firstName = firstName
		self.lastName = lastName

	def fullName(self):
		return ' '.join([self.firstName, self.lastName])