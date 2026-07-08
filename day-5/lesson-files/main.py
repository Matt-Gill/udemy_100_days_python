# For loops
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + ' pie')

print(fruits)

# Highest score

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

total_exam_score = sum(student_scores)
print(total_exam_score)

sum = 0
for score in student_scores:
    sum += score

print(sum)

max_student_score = max(student_scores)
print(max_student_score)

max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)

# For loops with Range function
for number in range(1, 10):
    print(number)

for number in range(1, 11):
    print(number)

for number in range(1, 11, 3):
    print(number)

total = 0
for number in range(1, 101):
    total += number

print(total)