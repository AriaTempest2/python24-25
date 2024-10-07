def multiply():
    lower = int(input("Enter the Lower Bound "))
    upper = int(input("Enter the Upper Bound "))

    x = lower
    y = upper

    theProduct = ( x*y )
    for number in range(lower * upper, upper):
        theProduct += number (x*y)
    print(theProduct)

def add():
    lower = int(input("Enter the Lower Bound "))
    upper = int(input("Enter the Upper Bound "))

    a = lower
    b = upper

    theProduct = ( a+b )
    for number in range(lower * upper, upper):
        theProduct += number (a+b)
    print(theProduct)

def divide():
    lower = int(input("Enter the Lower Bound "))
    upper = int(input("Enter the Upper Bound "))

    e = lower
    f = upper

    theProduct = ( e//f )
    for number in range(lower * upper, upper):
        theProduct += number (e//f)
    print(theProduct)

def subtract():
    lower = int(input("Enter the Lower Bound "))
    upper = int(input("Enter the Upper Bound "))

    c = lower
    d = upper

    theProduct = ( c-d )
    for number in range(lower * upper, upper):
        theProduct += number (c-d)
    print(theProduct)

answer = input("What Math do you want to do? please choose between add, subtract, multiply or divide ")
if answer == "divide":
    divide()
if answer == "multiply":
    multiply()
if answer == "add":
    add()
if answer == "subtract":
    subtract()
