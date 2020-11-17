# To get input from an user we use the input() function
name = input('Insert your name: ')
print(name)

# input() function interprets everything the user inserts as a string
# If we want to use the input as a number then we have to utilize the
# function int()
age = input("How old are you? ")
age = int(age)
print(age)

if age > 18:
    print('You\'re good to go.')
else:
    print('Wait to grow up.')

# In Python we can use the while loop
number = 1;

while number <= 10:
    print('-' + str(number) + '-', end=' ')
    number = number + 1
print('--------')

# As in other languages we can use flags
active = True

print('Insert a number. Press \'q\' anytime to quit')
while active:
    message = input('Enter number: ')
    if message == 'q':
        active = False
    else:
        print(message)

# We can use the break instruction to terminate the execution of a loop
while True:
    food = input("Enter favourite food: ")
    if food == 'quit':
        break
    else:
        print(food)

# As in other programming languages we can use the continue
# instruction - we skip the rest of the code inside a loop 
# for the current iteration only. Loop continues with the
# next iteration

for number in range(1, 10):
    if number % 2 == 0:
        continue
    print(number)

# To exit an infinite loop we use CTRL+C

# By using a while loop we can iterate over the elements of a list,
# extract the values and insert them into a dictionary/list
customers = ['Jim', 'Brian', 'Alice', 'Kate']
potentialCustomer = []

while customers:
    value = customers.pop()
    potentialCustomer.append(value)
print(potentialCustomer)

# Also by using while loop we can iterate over a list and eliminate
# the values that we don't want (clean the list)
numbers = [33, 22, 1, 2, 54, 10, 37, 33, 2, 7, 18, 2, 190, 221, 2]

while 2 in numbers:
    numbers.remove(2)
print(numbers)

