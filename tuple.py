#TODO tuple

#namedtuple
from collections import namedtuple

#Is initialized as a class
#Note: typename must follow regular class name rules, such as:
#	can't start with a number (e.g. '3Dpoint')
#	can't be same as a keyword (return, pass, etc.)
Point = namedtuple('point3D', ['x', 'y', 'z'])

#Instantiate with positional or keyword arguments
p = Point(3, 6, 0)
p = Point(3, 6, z = 10)

#Getting values
print(p[0])
print(p.x)
#Supports unpacking
print(*p, sep=', ')

#Is iterable
for coord in p:
	print(coord, end=', ')
print()


#Is immutable
try:
	p[0] = 16
except TypeError as e:
	print(e)

try:
	p.x = 16
except AttributeError as e:
	print(e)


#Has a __repr__
print(p)