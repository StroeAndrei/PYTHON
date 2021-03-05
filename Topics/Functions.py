# The basic sintax to create a function
def greet():
    print("Hello")

# Call the function
greet()

# Function with an argument
def greet(user):
    print("Hello, " + user.title() + "!")

greet("Bob")

# Usually when we define a function the variable we specify in the
# function definition is called a parameter and when we call the
# function we refer to it as an argument

# Ex: 
# def func(number) --> parameter
# func(8) --> argument

# Sending arguments to a function can be done in multiple ways:
# 1. Positional arguments
# - the order of the used arguments
# - matching of parameters when the function is defined and the
# arguments when the function is called
def some_pet(animal_type, pet_name):
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

some_pet('bird', 'puf')

# When we call the function above we specify the arguments
# in the order set in the function definition

# 2. Keyword arguments 
# A keyword argument is a name+value pair that we send
# to a function. 
def some_pet(animal_type, pet_name):
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

some_pet(animal_type='cat', pet_name="fuzzy")

# Python assigns the value 'cat' to the animal_type parameter
# In this case, the order doesn't matter anymore because we 
# explicitly specify the name-value pairs
some_pet(pet_name="fuzzy", animal_type="cat")

# 3. Implicit values
# We can define an implicit value for each parameter
def some_pet(pet_name, animal_type="turtle"):
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

some_pet(pet_name="William")

# The implicit value for animal_tye is 'turtle' so it's no longer
# required for us to specify it when we call the function

# If we want another value then we specify it when we call the function
some_pet(pet_name="bobi", animal_type="dog")

# Obs: When we use implicit values, the parameters with implicit values
# have to be listed after the parameters that don't have implicit values
# This allows Python to interpret positional arguments correctly

# Returning values
def format_name(fname, lname):
    return fname + " " + lname

print(format_name('Jim', 'Jones'))

# Optional arguments
def format_name(fname, lname, middle_name=''):
    if middle_name:
        return fname + ' ' + middle_name + ' ' + lname
    else:
        return fname + ' ' + lname

print(format_name('Jim', 'Jones', 'Doe'))

# Returning a value as a dictionary
# A function can return a list or dictionary
def build_user(fname, lname, username, email):
    user = {
        'fname': fname.title(),
        'lname': lname.title(),
        'username': username,
        'email': email
    }
    
    return user

user_1 = build_user('bob', 'beans', 'beans_90', 'beans@yahoo.com')
print(user_1)

# Sending a list to a function
def greet_users(users):
    for user in users:
        print("Hello " + user + "!")

greet_users(['Bob', 'Mike', 'Jim', 'Mary'])

# Modifying a  list in a function
numbers = [2, 32, 11, 19, 90, 22, 7, 14, 17, 34, 33]
even_numbers = []

def is_even(number):
    if number % 2 == 0:
        return True
    else: 
        return False

def move_evens(fromList, toList):
    tempNumList = fromList[:]
    for number in tempNumList:
        if is_even(number):
            toList.append(number)
            fromList.remove(number)
            
move_evens(numbers, even_numbers)
print(numbers)
print(even_numbers)

# If we want to avoid the modification of a list, we send
# a copy to the function
numbers2 = [2, 3, 1, 8, 22, 12, 9]
even_numbers2 = []

move_evens(numbers2[:], even_numbers2)
# the first list has the initial values
# after we call the function
print(numbers2) 
print(even_numbers2)

# When we don't know  beforehand the number of arguments 
# we want to send to a function -> use *

def eat(*food):
    print(food)

eat("cookie")
eat("chocolate", "salad", "bread")

# Python will build an empty tuple called food
def eat(*food):
    for fd in food:
        print(": " + fd)

eat("cookie")
eat("fried chicken", "cheese", "tomatoes")

# Combining arbitrary with positional arguments
# Obs: The parameter that accepts an arbitrary number of arguments
# has to be specified at the end of the function definition
def prepare_food(nrOfFoodDishes, *mainIngredients):
    print("Preparing a number of " + str(nrOfFoodDishes) + 
            " food dishes that contain as main ingredients: ")
    for ingredient in mainIngredients:
        print(ingredient)

prepare_food(12, 'chicken', 'beef', 'cheese')
prepare_food(5, 'fish', 'chocolate')

# Using a variable number of keyword arguments
# We want to accept an arbitrary number of arguments but we
# don't know beforehandwhat kind of information will be sent
# to the function. In this case we can write functions that
# accept key-value pairs in the function call

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('jim', 'jones', age='12', username='jimjones76')
print(user_profile)


# A function can serve as an iterator, as long as it can produce elements
# at different moments of its execution using the keyword yield
def all_pairs(L):
    n = len(L)
    for i in range(n):
        for j in range(i + 1, n):
            yield (L[i], L[j])

test = all_pairs([1, 2, 3, 4, 5])
print(test.next)

