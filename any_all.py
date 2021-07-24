#Basic syntax
#With an iterable
anyTrue = any((True, False))	#Tuple
allTrue = all([True, True])		#List
print(anyTrue, allTrue)

#With an iterator
iterator = (v > 0 for v in [-1, 2, 0, 5])
anyTrue = any(iterator)
allTrue = all(iterator)
print(anyTrue, allTrue)

#Can also do it directly in the function without extra parentheses
allTrue = all(v > 0 for v in [1, 2, 3])
print(allTrue)

anyTrue = any((True, False, True, False))
allTrue = all((True, True, True))
noneTrue = not any((False, False, False))

print(anyTrue, allTrue, noneTrue)

#Edge cases
emptyHasAnyTrue = any(())	#False
emptyHasNoFalse = all(())	#True
print(emptyHasAnyTrue, emptyHasNoFalse)

#Short-circuit

def giveBool():
	bools = [True, True, False, False, True, False]

	for i, b in enumerate(bools):
		print(f'Iteration {i}')
		yield b

any(giveBool())
print('Found a True, stopping iteration')

all(giveBool())
print('Found a False, stopping iteration')