n = [3, 5, 7]

def print_list(x):
    for i in range(0, len(x)):
        print(x[i])

print_list(n)

# Don't forget to return your new list!
def double_list(x):
    for i in range(0, len(n)):
        x[i] = x[i] * 2
    return x

print(double_list(n))

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

y = range(6)
print("y: %s" % y)

n = [3, 5, 7]

def total(numbers):
    result = 0
    for n in numbers:
        result += n
    return result

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
    result = []
    for numbers in lists:
        for number in numbers:
            result.append(number)
    return result

print(flatten(n))
