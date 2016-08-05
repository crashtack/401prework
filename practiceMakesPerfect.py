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

# print('total = {}'.format(scrabble_score("Helix")))

def censor(text, word):
    new = '*' * len(word)
    new
    text = text.replace(word, new)
    return text

# print(sensor('this hack is wack hack', 'hack'))

def count(sequence, item):
    count = 0
    for i in sequence:
        if i == item:
            count += 1
    return count

# print(count([4, 'foo', 5, 'foo'],5))

def purify(l):
    output = []
    for i in l:
        if i % 2 == 0:
            output.append(i)
    return output

# print(purify([1,2,3,4,5,6,7,8,9,10]))

def product(l):
    total = 1
    for i in l:
        total = total * i
    return total

# print(product([4,5,5]))

def remove_duplicates(l):
    new = []
    for e in l:
        if e not in new:
            new.append(e)
    return new

# print(remove_duplicates([1,1,1,2,3,4,4,4,5,6,7,7,8,8,0,0]))

def median(l):
    new_list = sorted(l)
    # print(new_list)
    output = 0
    med = 1.01

    if len(new_list) % 2 == 0:
        index = int(len(new_list) / 2)
        # print('index {}'.format(index))
        med = (new_list[index - 1] + new_list[index]) / 2.0
        # print(new_list[index - 1])
        # print(new_list[index])
    else:
        med = new_list[int(len(new_list)/2)]

    return med

print(median([1,8,3,9,1,1]))
print(median([1,8,3,7,9,1,1]))
