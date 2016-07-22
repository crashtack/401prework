def make_out_word(out, word):
    return out[0:2] + word + out[2:]

print(make_out_word('<<>>','hello'))

def extra_end(str):
    return str[-2:] * 3

print(extra_end('ab'))
print(extra_end('asdfg'))

def first_two(str):
    # if len(str) < 2:
    #     return str
    # else:
    return str[:2]

print(first_two('Hello'))
print(first_two('absdfre'))
print(first_two('ab'))
print(first_two('x'))
