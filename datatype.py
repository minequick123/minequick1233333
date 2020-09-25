#Built-in Data types

"""
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:
"""


#Text type: str

# Numeric Types: int, float, complex

# Sequence Types: list, tuple, range

# Mapping Type: dict

# Set Types: set, frozenset

# Boolean Type: bool

# Binary Types: bytes, bytearray, memoryView

"""
GETTING THE DATA TYPE 

You can get the data type of any object by using the "type()" function.
"""

# EXAMPLE

# print the data of the variable x

x = 5
print(type(x)) # int

x = "Hello World"
print(type(x)) # str

x = 20.5
print(type(x)) # float

x = 1j
print(type(x)) # complex

x = ["apple", "banana", "Cherry"]
print(type(x)) # list

x = ("apple", "banana", "cherry")
print(type(x)) # tuple

x = range(6)
print(type(x)) # range

x = {"name": "John", "age": 36}
print(type(x)) # dict

x = frozenset({"apple", "banana", "cherry"})
print(type(x)) # frozenset

x = True
print(type(x)) # bool

x = b"Hello"
print(type(x)) # bytes

x = bytearray(5)
print(type(x)) # bytearray

x = memoryview(bytes(5))
print(type(x)) # memoryView













