# List definition
numbers = [90, 1, 33, 12]

# Add an element in a list = append() method
numbers.append(101)

# Insert an element at a specified index
numbers[0] = "Word"

# Count the number of elements in a list - len() funtion
numberOfElements = len(numbers)
print(numberOfElements)

# Delete an element from a list
# We use the del operator
del numbers[0]
print(len(numbers))

# Extract last element from a list
# OBS: we modify the list
lastElement = numbers.pop()
print(lastElement)

# Delete a custom value - remove() method
numbers.remove(33)
print(numbers)

# Sort elements of a list - sort() method
# OBS: it modifies the list
nums = [4, 1, 0, 11, 34, 89, 99, 101, 22]
nums.sort()
print(nums)

# Reverse sorting - from large to small values
nums.sort(reverse=True)
print(nums)

# Sort without modifying the initial list
# We use the sorted() function
# For reverse order we use: sorted(numbers, reverse=True)
numbers = [9, 4, 0, 1, 33, 43, 21, 60, 75]
sortedNumbers = sorted(numbers)
print(sortedNumbers)

# To invert the elements in a list we use reverse() method
aFewNumbers = [8, 89, 0]
aFewNumbers.reverse()
print(aFewNumbers)

# Iterate over the elements of a list
# We use the "for in" loop
letters = ['A', 'S', 'Z', 'C']
for letter in letters:
    print(letter)

# Automatic generation of values from an interval
# range() function
squares = []
for number in range(1, 21): # OBS: we want 1 to 20, 21 is not included
    square = number**2
    squares.append(square)

print(squares)

# Construction of a list with range() it's done by using the list() function
numbers = list(range(1, 101))
print(numbers)

# If we want to set an interval between numbers we use a third parameter
numbers = list(range(0, 101, 10)) # 0 10 20 ... 100
print(numbers)

# Popular functions when working with lists
elements = [1, 2, 3]
print(sum(elements)) # Sum of the elements in a list
print(max(elements)) # Greatest element in a list
print(min(elements)) # Smallest element in a list

# List Comprehension - a concise method to construct a list
cubes = [value**3 for value in range(1, 101)]
print(cubes)

# List slicing - selection of a series of values
numbers = [90, 56, 88, 73, 52, 2, 11, 19]
print(numbers[1:5]) # 56 -> 52
print(numbers[:5]) # from the start of the list until the element with the index 4
print(numbers[0:]) # from the first element of the list until the last one
print(numbers[-3:]) # last 3 elements from the list

# Iterate over the elements of a list using List slicing
for number in numbers[:4]:
    print(number) # first 4 values

# Copying a list
initialList = ['ab', 'zy', 'cd']
copyOfInitialList = initialList[:]
print(copyOfInitialList)

# TOP slicing expressions for working with lists
# L = List
# L[i] = the ith element of L
# L[i:j] = the list of elements from index i to index j (but not 
# including j)
# L[:j] = the first j elements (not inlcuding j)
lst = [2, 3, 1, 43, 11, 43, 0]
print(lst[:5]) # form index 0 -> to index 4
# L[i:] = elements from i to n (not inluding i)
lst2 = [89, 32231, 42, 111, 322, 909]
print(lst2[4:])
# L[-3:] = tha last 3 elements
lst3 = ['a', 'e', 'r', 'b', 'c']
print(lst3[-3:])
# L[i:j:k] =  elements from the ith up to the jth (but not including
# j) taking only every kth element
lst4 = [32, 13, 112, 3131, 11, 0, 43]
print(lst4[0:6:1])
print(lst4[0:6:2])
# L[::2] = the elements of L with even indices
lst5 = [33, 21, 11, 90, 76, 65, 43, 89, 13]
print(lst5[::3]) # ::3 | index (divides)
print(lst5[::5])
# L[::-1] = the reverse copy of L
lst6 = ['a', 'b', 'c']
print(lst6[::-1])

# TOP methods for working with lists
# len(L) = number of elements in list L
# sorted(L) = returns a sorted copy of the list L
# L.sort() = sorts L in place
# L.count(c) = the number of occurences of c in L
# c in L = is the element c found in L
# L.append(c) = append c to the end of L
# L.pop() = extracts and returns the last element of L







