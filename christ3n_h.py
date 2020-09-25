if 5 > 2:
    print("five is greater than two")

#Python Variables.
#In Python, variables are created when you assign a value to it:
x = 5
y = "Hello World"

"""
Python has commenting capability for the purpose of in-code documentation.

Comments start with a #, and Python will render the rest of the line as a comment: 
"""

#this is a comment
print("Hello, World!")


#Comments can be placed at the end of a line, and Python will ignore the rest of the line:
print("Hello, World!") #this is a comment

#Comments does not have to be text to explain the code, it can also be used to prevent Python from executing code:
#print("Hello, World")
print("Cheers, Mate!")

#Python does not really have a syntax for multi line comments.
#To add a multiline comment you could insert a # for each line:

#This is a comment
#written in
#more than just one line
print("Hello, World!")

"""
Or, not quite as intended, you can use a multiline string.
Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string 
(triple quotes) in your code, and place your comment inside it:
"""

"""
This is a comment 
written in 
more than just one line
"""
print("Hello, World!")

# As long as the string is not assigned to a variable, Python will read the code, but then ignore it, and you have made a multiline comment.











