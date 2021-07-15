#Syntax: f'{[expression]![conversion]:[formatting]}'

#EXPRESSIONS

print(f'Hello {"dude"}')
print(f'2+3 is {2+3}')

place = 'world 🌎'
print(f'Hello {place}')

print()

#Print the expression and its result
print(f'{place=}')
print(f'{(2*3)+5=}')

print()


#CONVERSION

# !s calls the __str__() (default) function
print(f'String: {place!s}')

# !a calls the ascii() function
print(f'Ascii: {place!a}')

# !r calls the __repr__() function
print(f'Repr: {place!r}')

print()


#FORMATTING
# format	[[fill]align][sign][#][0][width][grouping_option][.precision][type]

name = 'Bobo'

#FORMAT: FILL, ALIGN, WIDTH
#Note: Width must be specified and greater than string len for fill and align to have an effect

#Fill: A single character
#Align:
# 	< right
#	> left
# 	^ center
#Width: Any integer

print(f'Meet {name:€>8}, my friend')
print(f'Meet {name:¢^10}, my friend')
print(f'Meet {name:.<11}, my friend')

print()

#FORMAT: SIGN

# +		Show sign for both positive/negative numbers
# -		Show sign for negative numbers only (default)
# space	Show - for negative numbers, space for positive numbers
print(f'{13:+}, {-13:+}')
print(f'{13:-}, {-13:-}')
print(f'{13: }, {-13: }')

print()

#FORMAT: GROUPING

# _ Separate thousands with _
# , Separate thousands with ,
num = 1378262.671

print(f'{num:_}')
print(f'{num:,}')

print()

#FORMAT: PRECISION

# .n Set precision to n digits (int)
num = 312.67189

print(f'{num:.2}')
print(f'{num:.3}')

print()

print(f'{num:.3g}')		#Use with 'g' type to work on integer part only
print(f'{num:.3f}')		#Use with 'f' type to work on decimal part only
print(f'{place:.3}')	#Use on strings to set characters

print()

#FORMAT: TYPE

# s		String format (default)
print(f'{place:s}')

print()

#FORMAT: TYPE [INTEGERS]

# d		Decimal (default)
# b		Binary
# c		Char
# o		Octal
# h		Hex (lowercase)
# H		Hex (uppercase)

num = 239

print(f'{num:d} decimal')
print(f'{num:b} binary')
print(f'{num:c} char')
print(f'{num:o} octal')
print(f'{num:x} hex')
print(f'{num:X} HEX')

print()


#FORMAT: TYPE [FLOATS/DECIMALS]

# e		Scientific notation
# e		Scientific notation (uppercase)
# f		Fixed-point notation
# F		Fixed-point notation (uppercase)
# g		General format (default)
# G		General format (uppercase)
# n		Number format (same as g, with locale settings for number separators)
# %		Percentage format (times 100)

num = 571823.9519389

print(f'{num:e} scientific notation')	#Default precision is 6
print(f'{num:E} scientific notation (uppercase)')
print(f'{num:f} fixed-point notation')	#Default precision is 6
print(f'{num:F} fixed-point notation (uppercase)')
print(f'{num:g} general format')
print(f'{num:G} general format (uppercase)')
print(f'{num:n} number format')
print(f'{num:%} percentage format')

print()

# Scientific notation with precision
# Precision applies to whole number
# Automatically rounds last coefficient digit
# Adds trailing zeroes if precision too high
print(f'{num:.1e} scientific precision 1')
print(f'{num:.4e} scientific precision 4')
print(f'{num:.10e} scientific precision 10')
print(f'{num:.16e} scientific precision 16')

print()

# Fixed-point notation with precision
# Precision applies to decimals only
# Automatically rounds last digit
# Adds trailing zeroes if precision too high
print(f'{num:.0f} fixed-point precision 0')
print(f'{num:.4f} fixed-point precision 4')
print(f'{num:.10f} fixed-point precision 10')
print(f'{num:.16f} fixed-point precision 16')

print()

# General format with precision
# Precision applies to whole number
# Automatically rounds last digit
# Adds trailing zeroes if precision too high
print(f'{num:.1g} general precision 1')
print(f'{num:.4g} general precision 4')
print(f'{num:.10g} general precision 10')
print(f'{num:.16g} general precision 16')

print()

# Percentage format with precision
# Precision applies to decimals only
# Automatically rounds last digit
# Adds superfluous digits if precision too high
print(f'{num:.1%} percentage precision 1')
print(f'{num:.4%} percentage precision 4')
print(f'{num:.10%} percentage precision 10')
print(f'{num:.16%} percentage precision 16')

print()

#Combining all format rules
num = 1327.67
print(f'{num:#^+20,.3f}')

print()


#Make a class formattable
from dataclasses import dataclass

@dataclass
class Text():
	value: str
	def __format__(self, format_spec):
		print(f'Do some formatting here')
		return self.value
		
message = Text('Hello world')
print(f'{message}')