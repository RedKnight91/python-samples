#Unpacking to a number of variables
#From list
personData = ['Joe', '21', 'Chicago']
name, age, city = personData
print(f'My name is {name}, age {age}, I live in {city}')

#From tuple
personData = ('Joe', '21', 'Chicago')
name, age, city = personData
print(f'My name is {name}, age {age}, I live in {city}')

#From set
#NOTE: This is not possible, as Set is not guaranteed to be created in order
personData = {'Joe', '21', 'Chicago'}
name, age, city = personData
print(personData)
print(f'My name is {name}, age {age}, I live in {city}')



#Swapping variables
x = 10
y = 20

x, y = y, x

#Useful for calculations without temp variables
#The right-side tuple values are evaluated with the 'old' values
#Then they're unpacked all at once when evaluations are over
xSpeed, ySpeed = 3, 10
isOutOfBounds = lambda x, y: x > 10 or y > 10

x, y, outOfBounds = (x + xSpeed, y + ySpeed, isOutOfBounds(x, y))


# Useful for function returns
giveXY = lambda: (5, 10)
x, y = giveXY()