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