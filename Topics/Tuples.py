# A tuple is similar to a list BUT
# A tuple is immutable - the values contained in a tuple
# cannot change

values = (8, 17, 20, 21)
# values[0] = 22 # Error - 'tuple' object does not support item assignment

# We can redefine a tuple
values = (3, 1, 0, -2) # this works fine
print(values)

# We can add lists as elements to a tuple
# We can modify the lists from the tuple

words = (['book', 'table', 'cake'], ['shoe', 'shirt', 'hat'])
print(words)
words[1][0] = 'socks'
print(words) # OK

