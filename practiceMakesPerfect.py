def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

def is_int(x):
    if x % 1 == 0:
        return True
    else:
        return False

def digit_sum(x):
    total = 0
    while x // 10:
        right_most = x % 10
        x = x // 10
        total = total + right_most

    total = total + x
    return total

# print(digit_sum(55555))

def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * (factorial(x - 1))

#print('factorial 3 = %i' % factorial(3))

def is_prime(x):
    for i in range(2,x):
        if x % i == 0:
            n = x % i
            #print('x: {} (x-1): {} i: {:>2} x % i: {}'.format(x, (x-1), i, n))
            return False
        else:
            n = x % i
            #print('x: {} (x-1): {} i: {:>2} x % i: {}'.format(x, (x-1), i, n))
    if x >= 2:
        return True
    else: return False

# for i in range(2,30):
#     print(i)

# for i in range(31):
    # print('{:>2} is a prime number: {}'.format(i,is_prime(i)))

def reverse(text):
    rev = []
    for i in range(len(text)):
        rev.append(text[-(i+1)])
    output = ''.join(rev)
    return output

# print(reverse("123456%^&*"))

def anti_vowel(text):
    vowels = 'aeiouAEIOU'
    for c in vowels:
        text = ''.join(text.split(c))
        # print(text)
    return text

# print(anti_vowel('Hello World'))

def scrabble_score(word):
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
    total = 0
    word = word.lower()
    for c in word:
        total = total + score['{}'.format(c)]
    #print(total)
    return total

print('total = {}'.format(scrabble_score("Helix")))
