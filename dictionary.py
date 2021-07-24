#Declaring a dict using 'dict'
peopleAge = dict(Joe=54, Sally=27, Gina=31)
print(peopleAge)

#Declaring a dict using { }
peopleAge = {'Joe':54, 'Sally':27, 'Gina':31}
print(peopleAge)

#Creating a dict using .fromkeys (sets all to same value)
peopleAge = dict.fromkeys(['Joe','Sally','Gina'], 0)
print(peopleAge)

#Dictionary from two lists
names = ['Joe', 'Sally', 'Gina']
ages = [54, 27, 31]

peopleAge = dict(zip(names, ages))
print(peopleAge)


#Getting a key's value
age = peopleAge['Joe']
print(age)

age = peopleAge.get('Joe')
print(age)

#Avoiding failure by returning default
age = peopleAge.get('Obama', 60)
print(age)

#Returns value or sets it to default if key not in dict
age = peopleAge.setdefault('Joe', 0)
print(age)

#Getting key list
people = peopleAge.keys()
print(people)
#Getting value list
ages = peopleAge.values()
print(ages)
#Getting key/value tuple list
tuples = peopleAge.items()
print(tuples)

#Popping key's value (deletes key)
age = peopleAge.pop('Sally')
print('Sally\'s age:', age, 'Remaining:', peopleAge)
#Popping last (LIFO) key-value tuple (deletes key)
while peopleAge:
	lastPerson = peopleAge.popitem()
	print(lastPerson, end=', ')
print()

#Setting a key's value
peopleAge['Joe'] = 55
print(peopleAge['Joe'])

#Setting a key's value only if not in dict
peopleAge.setdefault('Mike', 29)
print(peopleAge['Mike'])

#This won't work as the key is now already present
peopleAge.setdefault('Mike', 30)
print(peopleAge['Mike'])

#Setting key/value pairs with update
#Accepts kwargs
peopleAge.update(Sally=27, Gina=31)
#Accepts dicts
othersAge = {'Chuck':21}
peopleAge.update(othersAge)
#Accepts two-value tuple iterables
othersAge = [('Timmy', 3), ('Tommy', 6), ('Tammy', 4)]
peopleAge.update(othersAge)
print(peopleAge)


#Grouping
#We can do the same with defaultdict (more readable)
names = ['Sarah', 'John', 'Bob', 'Tim', 'Matt', 'Brad', 'Elise', 'Mandy', 'Richard']
lengthNames = {}
for name in names:
	key = len(name)
	lenNames = lengthNames.setdefault(key, [])
	lenNames.append(name)

print(lengthNames)

#defaultdict
#Instances a subclass of dict, taking in a factory function
#When getting a key which is not present, the key will be set to the default factory

from collections import defaultdict
from typing import ChainMap
peopleAge = defaultdict(int)
print(peopleAge)

#Getting an undefined key's value
print(peopleAge['Gina'])
#The key is now set to the default
print(peopleAge)

ages = defaultdict(int)		#defaults to 0
friends = defaultdict(list)	#defaults to []

#Setting custom default factory
constant_factory = lambda: None
countries = defaultdict(constant_factory)
print(countries['Italy'])

#Setting custom default factory with args
constant_factory = lambda name: lambda: f'Señor {name} no esta aqui'

deities = defaultdict(constant_factory('<missing>'))
print(deities['chosenGod'])


#Joining Dictionaries
dict1 = dict(name='Joe', age=16, job=None, married=False)
dict2 = dict(name='Joe', mother='Mary', father='Bob', age=18)
dict3 = dict(job='factory worker', wage=1300.00, dpisRequired=True)

#Replace matching keys when calling 'update'
fullDict = dict1.copy()
fullDict.update(dict2)
fullDict.update(dict3)
print(fullDict)

#'Chain' dictionaries, rightmost is base dict
fullDict = dict(ChainMap(dict3, dict2, dict1))
print(fullDict)