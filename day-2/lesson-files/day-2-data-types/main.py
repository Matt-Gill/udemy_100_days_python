#Data Types

#String

print("Hello"[4])

print("123" + "345")

#Integer

print(123 + 345)

print(123_456_789)

#Float

print(3.14159)

#Boolean

print(True)
print(False)

num_char = len(input("What is your name?\n"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

a = float(123)
print(type(a))

print(70 + float("100.5"))
print(str(70) + str("100"))

########################
# Mathematical Operators
########################

# 3 + 5
# 7 - 4
# 3 * 2
# 6 / 3
# 2 ** 3

# PEMDASLR
# ()
# **
# * /
# + -

print(3 * (3 + 3) / 3 - 3)

print(round(8 / 3, 2))

print(8 // 3)

print(type(8 // 3))
print(type(8 / 3))

result = 4 / 2
result /= 2
print(result)

score = 0

# User scores a point
score += 1
height = 1.80
isWinning = True
print(score)

#f-string
print(f"your score is {score}, your height is {height}, you are winning {isWinning}")