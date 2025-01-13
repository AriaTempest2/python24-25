def myFunction(a, b):
    print("\nVariable a is: ", a, ".")
    print("\nVariable a is: ", b, ".")
    exp1 = a ** b
    exp2 = b ** a
    print("\n", a, " to the power of ", b, "is: ", exp1)
    print("\n", b, " to the power of ", a, "is: ", exp2)

a = int(input("\nPlease enter a number between 1 and 10: "))
b = int(input("\nPlease enter a number between 1 and 10: "))

myFunction(a, b)



myVar1 = int(input("\nPlease enter a whole number: "))
myVar2 = int(input("\nPlease enter a whole number: "))