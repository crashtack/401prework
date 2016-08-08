"""
    A corney supermaket app
"""

prices = {"banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
    }

stock = {"banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
    }

for item in prices:
    print("item: " + item)
    print('price: %s' % prices[item])
    print('stock: %s' % stock[item])
    print()

total = 0

for item in prices:
    print("subtotal for %ss: %.2f" % (item,(prices[item] * stock[item])))
    total += (prices[item] * stock[item])

print('total: %.2f' % total)

def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] != 0:
            total += prices[item]
            stock[item] -= 1
        else:
            print('sorry, we are out of %ss.' % item)

    return total

groceries = ['banana', 'orange', 'apple']
bill = compute_bill(groceries)
print('bill = %.2f' % bill)
