# There are two variables, a and b from input
a = input("Input a number: ")
b = input("Input a number: ")

# Create a third variable to help switch the values
c = a
a = b
b = c

print("a: " + a)
print("b: " + b)

glass1 = "milk"
glass2 = "juice"

glass3 = glass1
glass1 = glass2
glass2 = glass3
