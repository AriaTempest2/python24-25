'''
Author: Gavin Hollinger
Program: Python
'''

# for blah in range(5):
#     print('blah')

# print('This is outside of the loop')

# number = 5
# exponent = 4
# product = 1

# for eachPass in range(exponent):
#     product = product * number
#     print(product, end=" ")
# print("\n")

product = 1

for count in range(1, 5):
    product = product * (count)

print(product)

lower = int(input("Enter the Lower Bound"))
upper = int(input("Enter the Upper Bound"))

theSum = 0

for number in range(lower, upper + 1):
    theSum = theSum + number

print("The summation between", lower , "and", upper, "is equal to", theSum)