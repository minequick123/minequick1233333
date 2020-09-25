# Assign Value to Multiple Variables

# Python allows you to assign values to multiple variables in one line:

x, y, z = "orange", "Bannana", "Cherry"
print(x)
print(y)
print(z)

# And you can assign the same value to multiple variables in one line:

x = y = z = "orange"
print(x)
print(y)
print(z)

"""
Output Variables

The Python 'print' statement is often used to output variables.

To combine both text and a variable, Python uses the '+' character:
"""


x = "awesome"
print(x)


# You can also use the '+' character to add a variable to another variable:

x = "Python is "
y = "awesome"
z = x + y
print(z)

# For numbers, the + character works as a mathematical operator:

x = 5
y = 10
print(x + y)

# if you try to combine a string and a number, python will give u an error.

"""
variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

Example:
"""

# Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()


"""
If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 
The global variable with the same name will remain as it was, global and with the original value.
"""
# Create a variable inside a function, with the same name as the global variable

x = "wild"

def myfun2():
    x = "fantastic"
    print("Python is " + x)

myfun2()

print("Python is " + x)


"""
The global Keyword

Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.

"""

#EXAMPLE:

#if you use the global keyword, the variable belongs to the global scope.


def func():
    global x
    x = "black"

func()

print("Christian is " + x)

#EXAMPLE 2

print("why am i so " + x)

#Also use the 'global' keyword if you want to change a global variable inside the function.


#EXAMPLE:

# To change the value of a global variable inside a function, refer to the variable using the 'global' keyword.

b = "super"

def myfunc():
    global b
    b = "orange"

myfunc()

print("Python is " + x)









