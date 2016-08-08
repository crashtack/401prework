""" This is a Pig Latin Translator, it will:
    [] Ask the user to input a word in English.
    [] Make sure the user entered a valid word.
    [] Convert the word from English to Pig Latin.
    [] Display the translation result.
"""

print('Welcome to the Pig Latin Translator!')

original = input("Enter a word: ")

if len(original) > 0 and original.isalpha():
    print(original)
else:
    print("empty")

pyg = 'ay'
word = original.lower()
first = word[0]
new_word = word + first + pyg
new_word = new_word[1:len(new_word)]
print(new_word)
