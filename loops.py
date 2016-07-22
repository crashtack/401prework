"""    Loop operations
        while True:         # loops while true
        for i in range(3):  # loops 3 times
        for n in numbers:   # loops for each element in list numbers
        for key in set:     # loops for each key in a set
        for index, item in enumerate(choices): # loops for each item in list choices, and returns index
        for a, b in zip(list_a, list_b):    # Creates a pair of elements when passed 2 lists. stops at the end of the shorter list
        for f in fruits:
        else:               # runs else after for unless 'break' is used
"""

from random import randint

count = 0
while count < 3:
    num = randint(1, 6)
    print (num)
    if num == 5:
        print("Sorry, you lose!")
        break
    count += 1
else:
    print("You win!")

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
    guess = int(input("Your guess: "))
    if guess == random_number:
        print("You win!")
        break
    guesses_left -= 1
else:
    print("You lose.")

hobbies = []

# Add your code below!
for i in range(3):
    hobbies.append(input("Name one of your Hobbies: "))
print(hobbies)

word = "eggs!"

# Your code here!
for c in word:
    print(c),

d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    # Your code here!
    print(key + " " + d[key])

choices = ['pizza', 'pasta', 'salad', 'nachos']

print('Your choices are:')

for index, item in enumerate(choices):
    print(index, item)

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    # Add your code here!
    if a >= b:
        print(a)
    else:
        print(b)

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
    else: print 'A', f
else:
    print 'A fine selection of fruits!'

animals = ['dog', 'cat', 'mouse', 'bird', 'squerril']

for animal in animals:
    if animal == 'squerril':
        print('A squerril is an animal but would not make a good pet')
    else: print('A %s would make a good pet' % animal)
else:
    print('now pick one')
