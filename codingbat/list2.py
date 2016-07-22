def count_evens(nums):
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count

# print("3:%i" % count_evens([2, 1, 2, 3, 4]))
# print("3:%i" % count_evens([2, 2, 0]))
# print("0:%i" % count_evens([1, 3, 5]))

def big_diff(nums):
    mx = nums[0]
    mn = nums[0]
    for num in nums:
        mx = max(mx,num)
        mn = min(mn,num)
        # print("max: %i" % mx)
        # print("min: %i" % mn)

    return mx - mn

# print(big_diff([10,3,5,6]))
# print(big_diff([7, 2, 10, 9]))
# print(big_diff([2, 10, 7, 2]))

"""

Return the "centered" average of an array of ints, which we'll say is the
mean average of the values, except ignoring the largest and smallest values
 in the array. If there are multiple copies of the smallest value, ignore
 just one copy, and likewise for the largest value. Use int division to produce
 the final average. You may assume that the array is length 3 or more.

centered_average([1, 2, 3, 4, 100]) -> 3
centered_average([1, 1, 5, 5, 10, 8, 7]) -> 5
centered_average([-10, -4, -2, -4, -2, 0]) -> -3
"""

def find_max(nums):
    max_index = 0
    mx = nums[0]
    for num in nums:
        mx = max(mx,num)
        print('max: %i' % mx)
    return mx

def centered_average(nums):
    mx = nums[0]
    mn = nums[0]
    for num in nums:
        mx = max(mx,num)
        mn = min(mn,num)

    nums.remove(mx)
    nums.remove(mn)

    return sum(nums) / len(nums)

# print("[1,2,3,45,100] Average: %i" % centered_average([1,2,3,4,100]))
# print("[1, 1, 5, 5, 10, 8, 7] Average: %i" % centered_average([1, 1, 5, 5, 10, 8, 7]))
# print("[-10, -4, -2, -4, -2, 0] Average: %i" % centered_average([-10, -4, -2, -4, -2, 0]))

def sum13(nums):
    index_of_13 = -2
    total = 0
    for index, num in enumerate(nums):
        print("Index: %i Num: %i Total: %i" % (index,num,total))
        if num == 13:
            index_of_13 = index
        elif index != (index_of_13 + 1):
            total += num
    return total

# print("sum13([1, 2, 2, 1]) should equal: 6 ---> %i" % sum13([1, 2, 2, 1]))
# print("sum13([1, 1]) should equal: 2 ---> %i" % sum13([1, 1]))
# print("sum13([1, 2, 2, 1, 13]) should equal: 6 ---> %i" % sum13([1, 2, 2, 1, 13]))
# print("sum13([1, 2, 2, 1, 13, 14, 15]) should equal: 21 ---> %i" % sum13([1, 2, 2, 1, 13, 14, 15]))

"""
Return the sum of the numbers in the array, except ignore sections of numbers
least one 7). Return 0 for no numbers.

sum67([1, 2, 2])-> 5
sum67([1, 2, 2, 6, 99, 99, 7]) -> 5
sum67([1, 1, 6, 7, 2]) -> 4
"""
def sum67(nums):
    index = -2
    in67 = False
    total = 0
    for num in nums:
        if num == 6:
            in67 = True
        if in67 == False:
            total += num
        if num == 7:
            in67 = False
    return total

# print('[1,2,3] equals: 6 ---> %i' % sum67([1,2,3]))
# print('[1,2,2,6,99,99,7] equals: 5 ---> %i' % sum67([1,2,2,6,99,99,7]))
# print('[1,1,6,8,9,7,2] equals: 4 ---> %i' % sum67([1,1,6,8,9,7,2]))

def has22(nums):
    answer = False
    index_of_2 = -2
    for index, num in enumerate(nums):
        if (index + 1) < len(nums):
            if num == 2 and nums[index + 1] == 2 and (index + 1) <= len(nums):
                answer = True
                break
    return answer

print('has22([1,2,2]) is True= %s' % has22([1,2,2]))
print('has22([1,2,1,2]) is False= %s' % has22([1,2,1,2]))
print('has22([2,1,2]) is False= %s' % has22([2,1,2]))
print('has22([2,2,1,2]) is True= %s' % has22([2,2,1,2]))
