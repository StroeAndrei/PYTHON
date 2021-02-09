# variable declaration
message = "Hello"

# output the value of a variable
print(message)

# output with uppercase letters
print(message.upper())

# output with lowercase letters
print(message.lower())

# output with first letter uppercase
print(message.title())

# string concatenation
# we use "+" to concatenate strings
print("Hello" + "!!!")

# OBS: if we want to output numbers as strings we use str() function
# Example:
# print(45 + " words") # error = TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(str(45) + " words") # OK

# In Python we have 4 basic types: Booleans, integers, floating-point
# numbers and character strings
# The functions (construnctors in fact): bool, int, float, str
# allow the conversion of an object to the basic types
# In contrast with C, strings are IMMUTABLE (can't directly modify a
# character of a string)

# In Python the principal complex data structures are dictionaries,
# sets, lists and n-tuples.
# These structures are called containers. The functions: dict, set,
# list and tuple allow the conversion of an object into one of these
# structures

myName = 'Bob'
myNameChars = list(myName)
print(myNameChars)
print(myNameChars[1])

getBackName = ''.join(myNameChars)
print(getBackName)

# separatorul '' poate fi inlocuit si cu '-', '*' etc


