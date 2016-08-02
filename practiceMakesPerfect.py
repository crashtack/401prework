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

for i in range(31):
    print('{:>2} is a prime number: {}'.format(i,is_prime(i)))
