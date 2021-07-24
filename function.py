#Basic function
def giveNumber():
	return 3

def checkTrue(val):
	return val == True


#Default argument value (set if argument is not passed)
def sayFullName(first, last='Smith'):
	print(first, last)

#Mutable Default Argument
#Defaults are created at first function evaluation
#If default has to be created each time, we must do so in the function body
def addToParty(role, party=[]):
	party.append(role)
	return party

party1 = addToParty('mage')
party2 = addToParty('knight')
party3 = addToParty('rogue')
#The same list gets returned every time
print(party1 is party2 is party3)
#All the items were added to that list
print(party3)

#This version will work correctly
def addToParty(role, party=None):
	party = party if party else []
	party.append(role)
	return party

#Calling function with named arguments
def calcGain(start, end, currency, time):
	print(f'You made {end - start} {currency}s in only {time}.')

#Order can be as we wish, as long as they're named
calcGain(currency='dollar', time='10 seconds', start=3, end=10)
#We can pass some in order and name the rest
calcGain(2, 12, currency='euro', time='8 seconds')

#Passing an indefinite number of argument as 'args'
def log(*args):
	#args is an immutable tuple, can be named anything
	print(args)

log('Cheese', 'Bread', 'Pizza', 'Banana')

#Passing named arguments as 'kwargs'
def log(**kwargs):
	#kwargs is a MUTABLE dict, can be named anything
	print(kwargs)

log(name='Joe', income=1300.00, married=True)

#Anonymous function
giveNumber = lambda: 3
checkTrue = lambda val: val == True