#LIST COMPREHENSION
# Syntax: [x for x in []]

numbers = [0, 1, 2, 3, 4]

# Simple expression
allNumbers = [n for n in numbers]
print(allNumbers)

# Complex expression
squaredNumbers = [n*n for n in numbers]
print(squaredNumbers)

# Functions
process = lambda n: str(n) + '$'
processedNumbers = [process(n) for n in numbers]
print(processedNumbers)

# Conditional
evenNumbers = [n for n in numbers if not n % 2]
print(evenNumbers)

# Combined
letters = ['a', 'b', 'c']
combos = [(l, n) for l in letters for n in numbers]
print(combos)

# Nested
itemStats = [[3, 1, 0], [4, 2, 4], [0, 2, 4]]
# The nesting order is left-right, as it would be top-down in nested for loops
allStats = [stat for item in itemStats for stat in item]
print(allStats)

# Complex conditional
oddNumbers = [n for n in numbers if n not in [n for n in numbers if not n % 2]]
print(oddNumbers)


# DICT COMPREHENSION
# Syntax: {key: value for key, value in []}

names = ['Joe', 'Bob', 'Mary']
ages = [33, 76, 26]

# Simple expression
people = {name: age for (name, age) in zip(names, ages)} # Same as dict(zip(names, ages))
print(people)

# Conditional
people = {name: age for (name, age) in zip(names, ages) if name != 'Bob'}
print(people)

# GENERATOR COMPREHENSION
# Syntax: (x for x in [])
squareGenerator = (n*n for n in numbers)
[print(n) for n in squareGenerator]

# SET COMPREHENSION
# Syntax: {x for x in []}
numbers = [0, 1, 1, 2, 3, 3, 3, 4]
set = {n for n in numbers}
print(set)