# if/else/elif
# if = check if an expression is true

foodList = ['pizza', 'salad', 'fried chicken', 'hamburger']

for food in foodList:
    if food == 'pizza':
        print(food.upper())
    else:
        print(food.title())

# Comparing strings
# == for =
# != for inequality
drink = 'water'

if drink != 'coffee':
    print('NO')

# Comparing numbers
age = 90

if age != 20:
    print('Not the right age')

# Verify if a value is in a list
# We use the keyword "in"
numbers = [32, 11, 9, 32, 47, 55, 67, 101]
num = 32

if num in numbers:
    print(str(num) + ' is in the list')

# Verify if a value is not in a list
users = ['jim', 'bob', 'diana', 'simon', 'tim']
user = 'bianca'

if user not in users:
    users.append(user)
print(users)

# Complete 'if' example
age = 22

if(age < 18):
    print('Too young!')
elif (age >= 18 and age <= 30):
    print('Young')
else:
    print('Old')

# Obs: li = [] -> will be false when empty