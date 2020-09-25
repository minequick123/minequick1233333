# Python Numbers:

"""
There are three numeric types in Python:

- int
- float
- complex

Variables of numeric types are created when you assign a value to them:

"""

x = 1 # int
y = 2.8 # float
z = 1j # complex

# To verify the type of any object in Python, use the "type()" function:

print(type(x))
print(type(y))
print(type(z))

# Int

# int, or integer, is a whole number, positive or negative, without decimals, of unlimited length

# integers:

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# FLOAT

# Float, or floating point number, positive or negative, containing one or more decimals

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# Float can also be numbers with an "e" to indicate the power of 10

# FLOATS:

x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

# Complex

# Complex numbers are written with a "j" as the imaginary part:

# Complex:

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Type Conversion

# you can convert from one type to another with the "int()", "float()", and "complex()" methods:

# EXAMPLE:

# Convert from one type to another.

x = 1  # int
y = 2.8  # float
z = 1j  # complex

# convert from "int" to "float":
a = float(x)

# convert from "float" to "int":
b = int(y)

# convert from "int" to "complex":
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Note: you cannot convert complex numbers into another number type.

"""
Random Number:

Python does not have a "random()" function to make a random number, but python has a built-in module called 
"random" that can be used to make random numbers.
"""

# EXAMPLE

# import the random module, and display a random number between 1 and 9:

import random
print(random.randrange(1, 10))

# In our Random Module Reference you will learn more about the Random module.

