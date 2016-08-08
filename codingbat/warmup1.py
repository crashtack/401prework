def sleep_in(weekday, vacation):
    if vacation == True:
        return True
    elif weekday == False:
        return True
    else:
        return False

print('False, False: %s' % sleep_in(False, False))
print('True, False: %s' % sleep_in(True, False))
print('False, True: %s' % sleep_in(False, True))

def diff21(n):
    diff = 21 - n
    diff = abs(diff)
    if n > 21:
        return diff * 2
    else:
        return diff

print('22: %i' % diff21(22))
print('25: %i' % diff21(25))
print('30: %i' % diff21(30))

def parrot_trouble(talking, hour):
    if (hour < 7 or hour > 20) and talking:
        return True
    else: return False

print(parrot_trouble(True, 6))
print(parrot_trouble(True, 7))
print(parrot_trouble(False, 6))
print(parrot_trouble(True, 21))
