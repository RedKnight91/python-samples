values = list(range(0, 21))

# Syntax: [ start : stop ]
# Rules:
# 1. Positive 'start' and 'stop' values count from 0
# 2. Negative 'start' and 'stop' values count from 'len'
# 3. If 'start' is omitted, it defaults to 0 
# 4. If 'stop' is omitted, it defaults to 'len' 
# 5. First 'start' element is always included
# 6. Last 'stop' element is always excluded

print('[0]', values[0])
print('[-1]', values[-1])

# a[:]           # copy of the whole array
print('[:]', values[:])

# [start:]      # items start through the rest of the array
print('[3:]', values[3:])

# [:stop]       # items from the beginning through stop (excluded)
print('[:6]', values[:6])

# [start:stop]  # items start through stop (excluded)
print('[3:6]', values[3:6])

#Negative indices
# [-start:]      # items 'start' places from last through last
print('[-3:]', values[-3:])

# [:-stop]       # items from the beginning through 'stop' places from last (excluded)
print('[:-3]', values[:-3])

# [-start:-stop]  # items 'start' places from last through 'stop' places from last (excluded)
print('[-6:-3]', values[-6:-3])


# Out-of-range indices are not returned
print('[45:]', values[45:])


# Slicing can be performed on many iterable objects
print((1, 2, 3, 4, 5)[3:])
print('Hello'[3:])

try:
	print({1, 2, 3, 4, 5}[3:])
except:
	print('Cannot slice a set')