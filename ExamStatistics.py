grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
print("Grades:", grades)

def print_grades(grades):
    for grade in grades:
        print(grade)

# print_grades(grades)

def grades_sum(scores):
    sum = 0
    for score in scores:
        sum = sum + score
    return sum

# print('Sum: {}'.format(grades_sum(grades)))

def grades_average(grades):
    average = grades_sum(grades)/float(len(grades))
    return average

print('Average: {0:.2f}'.format(grades_average(grades)))
