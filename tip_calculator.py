# Meal Tip Calculator
"""
meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)
"""
import math
#from math import sqrt

def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print("With tax: %f" % bill)
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print("With tip: %f" % bill)
    return bill

meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

max(1,2,3,4)
min(1,2,3,4)
abs(-54)
print(type(4.3))
