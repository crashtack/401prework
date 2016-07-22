def double_char(str):
    out = ''
    for c in str:
        out += c * 2
    return out

# print(double_char('the'))
# print(double_char('Hi-There'))

# def double_char(str):
#   result = ""
#   for i in range(len(str)):
#     result += str[i] + str[i]
#   return result

def count_code(str):
    count = 0
    index = 0

    while index < len(str):
        if str.find('co',index) < 0:
            print('first if index: %i' % index)
            break
        else:
            index = str.find('co', index)
            print('index: %i' % index)
            if (index + 3) < len(str) and str[index + 3] == 'e':
                count += 1
                index += 4
            else:
                index += 2

    return count

# print("'nope' Should Return: 0 ---> %i" % count_code('nope'))
# print()
# print("'dddcoda code coue cod' Should Return: 2 ---> %i" % count_code('dddcoda code coue cod'))
# print()
# print("'codecode' Should Return: 2 ---> %i" % count_code('codecode'))
# print()
# print("'co' Should Return: 0 ---> %i" % count_code('co'))
# print()
# print("'coAcodeBcoleccoreDD' Should Return: 3 ---> %i" % count_code('coAcodeBcoleccoreDD'))

def count_hi(str):
    count = 0
    index = 0

    while index < len(str):
        if str.find('hi',index) < 0:
            break
        else:
            index = str.find('hi', index)
            count += 1
            index += 2
    return count

# print("'abc hi ho' should return: 1 ---> %i" % count_hi("abc hi ho"))
# print("'ABChi hi'' should return: 2 ---> %i" % count_hi("ABChi hi'"))
# print("'hihi' should return: 2 ---> %i" % count_hi("hihi"))

def end_other(a, b):
    a = a.lower()
    b = b.lower()

    if len(a) > len(b) and b ==  a[-len(b):]:
        # print('-len(b): %i' % -len(b))
        # print('a[-len(b):]: %s' % a[-len(b):])
        # if b ==  a[-len(b):]:
        return True
    elif a == b[-len(a):]:
        return True

    return False

# print("'Hiabc', 'abc' Should return: True ---> %s" % end_other('Hiabc', 'abc'))
# print("'bodddd', 'fdafdsaffsdf' Should return: False ---> %s" % end_other('bodddd', 'fdafdsaffsdf'))
# print("'abc', 'trefdsaabc' Should return: True ---> %s" % end_other('abc', 'trefdsaabc'))

def cat_dog(str):
    def count_hi(str, word):
        count = 0
        index = 0

        while index < len(str):
            if str.find(word,index) < 0:
                break
            else:
                index = str.find(word, index)
                count += 1
                index += 2
        return count

    if count_hi(str, 'cat') == count_hi(str, 'dog'):
        return True
    else: return False

# print(cat_dog('catdog'))
# print(cat_dog('catcat'))
# print(cat_dog('1cat1cadodog'))

def xyz_there(str):
    index = 0
    while index < len(str):
        if str.find('xyz', index) >= 0 and str[str.find('xyz',index) - 1] != '.':
            return True
        else:
            index += 3
    return False

print("xyz_there(abc.xyzxyz') → True: %s" % xyz_there('abc.xyzxyz'))
print("xyz_there('abcxyz') → True: %s" % xyz_there('abcxyz'))
print("xyz_there('abc.xyz') → False: %s" % xyz_there('abc.xyz'))
print("xyz_there('xyz.abc') → True: %s" % xyz_there('xyz.abc'))
