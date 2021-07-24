for i in range(6):
	print(i, end=' ')
print()

#Looping over list
colors = ['red', 'blue', 'green']
for color in colors:
	print(color, end=' ')
print()

#Looping over dict
#By default we get the key
people = {'Bob': {'age': 43}, 'Sally': {'age': 27}, 'Gina': {'age': 29}}
for personName in people:
	print(personName, end=' ')
print()

#Looping dict values only
for personData in people.values():
	print(personData, end=' ')
print()

#Looping whole dict items
for person in people.items():
	print(person, end=' ')
print()

#Looping over an iterable of tuples allows unpacking
for i, color in enumerate(colors):
	print(i, ':', color, end=' ')
print()

#Iterating two lists at once
people = ['Bob', 'Sally', 'Gina']
for person, color in zip(people, colors):
	print(person, '\'s favorite color is ', color, end=' ')
print()

#Reversed loop
for color in reversed(colors):
	print(color, end=' ')
print()

#Sorted loop
for color in sorted(colors):
	print(color, end=' ')
print()

#Reverse sorted loop
for color in sorted(colors, reverse=True):
	print(color, end=' ')
print()

#Custom sorted loop
#Takes a 1-argument callable as key arg
for color in sorted(colors, key=len):
	print(color, end=' ')
print()

#The argument can be a custom function or a lambda
people = {'Bob': {'age': 43}, 'Sally': {'age': 27}, 'Gina': {'age': 29}}
for personName in sorted(people, key=lambda name: people[name]['age']):
	print(personName, end=' ')
print()

#For can have an else clause at the end
for color in colors:
	if color == 'turquoise':
		print('Found a match')
		break
else:
	print('No match')

#Looping until a sentinel value is found in the iterable
import itertools
for i in itertools.takewhile(lambda i: i!= 6, range(999)):
	print(i, end=' ')
print()

#Looping until a sentinel value is returned from a function
import random
giveNum = lambda: random.randint(0,10)

for n in iter(giveNum, 4):
	print(n, end=' ')
print()