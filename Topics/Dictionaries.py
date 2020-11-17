# A dictionary is an unordered collection of elements

player = {
	'name': 'Mordem',
	'level': 100
}

# Accessing a value using the key
print(player['name'])

# Adding elements one after another
player = {}
player['name'] = 'Mordem'
player['level'] = 100

# Deleting an element from a dictionary
del player['level'];

# Iterate over the keys and values of a dictionary
user = {
	'username': 'billxyz',
	'firstname': 'bill',
	'lastname': 'beans'
}

for key, value in user.items():
	print('key: ' + key)
	print('value: ' + value)

# Iterate over the keys of a dictionary
fav_food = {
	'Bob': 'pizza',
	'Dan': 'chips',
	'Mary': 'cookies',
	'Colson': 'donuts'	
}

for person in fav_food.keys():
	print(person.title())

# If we don't specify a method, we're going to iterate over 
# the keys of the dictionary
for name in fav_food:
	print(name.title())

# We can compare the elements of a list with the  keys of a dictionary
users = ['James', 'Colson']

for name in fav_food.keys():
	if name in users:
		print('Found ' + name + ' in the favourite food list')

# Iterate over keys in order (sorted)
for name in sorted(fav_food.keys()):
	print(name, end=' ')
print()

# Iterate over the values of a dictionary
for food in fav_food.values():
	print(food)

# Iterare peste valorile unui dictionar fara duplicate
# Utilizam functia set()
# Un set este similar cu o lista, cu diferenta ca fiecare
# element din set trebuie sa fie unic
# The order of the elements in a set is random and elements are unindexed
subscriptions = {
	'Mark': 90.00,
	'Jim': 19.99,
	'Bob': 21.00,
	'Jimmy': 18.50,
	'Mary': 22.30,
	'Karl': 19.99,
	'Beth': 30.00,
	'Ben': 18.50
}

for subscription in set(subscriptions.values()):
	print(subscription)

# We can build a list of dictionaries
player_1 = {'name': 'Bob_123', 'level': 50}
player_2 = {'name': 'Simtec', 'level': 65}
player_3 = {'name': 'Kullban', 'level': 90}
player_4 = {'name': 'Krull', 'level': 42}

players = [player_1, player_2, player_3, player_4]

# To iterate over the elements of this list
for player in players:
	print(player)
print('----------')

# To iterate over a defined number of elements
for player in players[:2]:
	print(player)

# Using a list as a value in a dictionary
application = {
	'type': 'web',
	'technologies': ['javascript', 'css', 'html', 'php']
}

for tech in application['technologies']:
	print(tech)

# Using dictionaries as values in another dictionary
players = {
	'JimS32': {
		'level': 100,
		'class': 'barbarian'
	},

	'Simor': {
		'level': 40,
		'class': 'mage'
	}
}

for playerName, playerAttributes in players.items():
	print(playerName + ': ' + str(playerAttributes))