# PYTHON STRINGS:

# String Literals:

"""
String literals in Python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello"

You can display a string literal with the print() function:
"""

# EXAMPLE:

print("Hello")
print('Hello')

# Assign String to a Variable

# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

# EXAMPLE

a = "Orange"
print(a)

# MULTILINE STRINGS
# you can assign a multiline string to a variable by using three quotes:

# EXAMPLE:
# you can use three double quotes

a = """Jack and Jill went up the hill 
to fetch a pail of water.
"""
print(a)

# Or three single quotes:

a = '''Bob the builder, can we fix it?
Bob the builder, YESSS WE CAN!!!
'''
print(a)

# in the result, the line breaks are inserted at the same position as in the code.

"""
STRINGS ARE ARRAYS:

Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
"""

"""
Example

Get the character at position 1 (remember that the first character has the position 0):
"""

a = "Hello, World!!"
print(a[1])

# Slicing

"""
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.
"""

"""
Example

Get the characters from position 2 to position 5 (not included):
"""

b = "Hello, World!"
print(b[2:5])

"""
Negative Indexing:

Use negative indexes to start the slice from the end of the string: 
"""

"""
Example

Get the characters from position 5 to position 1 (not included), starting the count from the end of the string:
"""

b = "Hello, World!"
print(b[-5:-2])

# STRING LENGTH

# To get the length of a string, use the 'len()' function.

# EXAMPLE

# The 'len()' function returns the length of a string:

a = "Orange"
print(len(a))

# STRING METHODS:

# Python has a set of built-in methods that you can use on strings.

# EXAMPLE

# The 'strip()' method removes any whitespace from the beginning or end:

a = "Hello, World!"
print(a.strip())  # returns "Hello, World!"

# EXAMPLE

# The 'lower()' method returns the string in lower case:

a = "ORANGE MAN"
print(a.lower())

# EXAMPLE

# The 'upper()' method returns the string in upper case:

c = "man orange"
print(c.upper())

# EXAMPLE

# The 'replace()' method replaces a string with another string.

x = "Orange, Red!"
print(x.replace("O", "K"))

# EXAMPLE #2

y = "Super, Woman"
print(y.replace("o", "E"))


# EXAMPLE

# The 'split()' method splits the string into substrings if it finds instances of the separator:

f = "What, Now?"
print(f.split(","))  # returns ['What', 'Now?']


# CHECK STRING

# To check if a certain phrase or character is present in a string, we can use the keywords "in" or "not in".

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

# EXAMPLE

# Check if the phrase "ain" is NOT present in the following text:

txt = "The moon in sky "















