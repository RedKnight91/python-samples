num = 13

# Convert an integer to binary string
# Prefix is 0b
# Calls __index__()
print(bin(num))

# Formatting to include '0b' prefix
print(f'{num:#b}')

# Formatting to exclude '0b' prefix
print(f'{num:b}')

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Returns Boolean, True or False
# Value is converted using the standard truth testing procedure
print(bool(3))
print(bool(0))
print(bool(True))
print(bool('a'))
print(bool([]))

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Returns a mutable array of bytes
print(bytearray([1, 2, 3]))
print(bytearray('Hello', 'utf_8'))
print(bytearray(5))

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Returns an immutable sequence of bytes
print(bytes([1, 2, 3]))
print(bytes('Hello', 'utf_8'))
print(bytes(5))

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Converts Unicode index to character
# [32 - 47] ==> symbols
# [48 - 57] ==> 0-9 digits
# [58 - 64] ==> symbols
# [65 - 90] ==> A-Z letters
# [91 - 96] ==> symbols
# [97 - 122] ==> a-z letters
# [123 - ...] ==> symbols
print(chr(97))

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# TODO
complex()

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Converts an integer or string to floating point number
# Calls __float__(), falls back to __index__()
print(float(3))
print(float('-3'))
print(float('NaN'))
print(float('-infinity'))

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Converts an integer to lowercase hexadecimal string
# Prefix is '0x'
print(hex(255))
print(hex(-3))

# Format to lowercase, include '0x' prefix
print(f'{255:#x}')

# Format to lowercase, exclude '0x' prefix
print(f'{255:x}')

# Format to uppercase, exclude '0x' prefix
print(f'{255:X}')


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Converts a number or string to integer
# Calls __int__, __index__, or __trunc__
print(int(10.3))
print(int('-10'))
print(int())		# Returns 0

# Setting 'base' attr (default 10)
# In this case we can only pass a string
print(int('111', 2))

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Converts an integer to octal string
# Prefix is 0o
print(oct(num))
print(oct(-num))

# Formatting to include '0o' prefix
print(f'{num:#o}')

# Formatting to exclude '0o' prefix
print(f'{num:o}')

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Converts character to Unicode index
print(ord('a'))

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Converts an object to string
# Calls __str__, falls back to __repr__
print(str(num))
print(str([1, 2, 3]))
print(str(lambda x: x))