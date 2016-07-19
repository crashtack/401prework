"""
    List commands
    list = []           # empty list
    square_list.sort()
    list.index('duck')
    list.insert(index, 'duck') # shifts everything right
    list.remove('duck')
    list.append('dog')

    Dictionary Commands
    menu = {}           # Empty dictionary
    menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
    del zoo_animals['Unicorn']      # Removes key-value pair
"""
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]  # Third and fourth items (index two and three)
last   = suitcase[4:] # The last two items (index four and five)

print (first)
print (middle)
print (last)

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index('duck') # Use index() to find "duck"

# Your code here!
animals.insert(duck_index, 'cobra')
print animals # Observe what prints after the insert operation

animals.remove('emu')

my_list = [1,9,3,8,5,7]

for number in my_list:
    # Your code here
    print(number*2)

start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for num in  start_list:
    square_list.append(num**2)

square_list.sort()
print square_list

# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

# Your code here!
print(residents['Sloth'])
print(residents['Burmese Python'])

menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['Ham Sandwitch'] = 5.67
menu['BLT'] = 6.50
menu['Colorado Omlet'] = 9.50

print "There are " + str(len(menu)) + " items on the menu."
print menu

# key - animal_name : value - location
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']
print(zoo_animals)

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50

print(inventory)
