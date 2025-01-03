print("Logical operators example")

isRaining = False
isSunny = True

print(isRaining)
print(isSunny)

print("Logical operators example")

isWeekend = False
isHoliday = False

print(isHoliday and isWeekend)
print(isHoliday or isWeekend)
print(not isHoliday)
print(not isHoliday or isWeekend)
print(not isHoliday and isWeekend)

print("Comparison Operator examples")
x = 10
y = 20

print(x == y)
print(x != y)
print(x < y)
print(x >= y)
if x < y:
    print("This is the if code")
else:
    print("This is the Else code")

'''
If statement: Lets the program decide what code to run based on a condition
'''

num1 = 5
num2 = 2

if num2 > num1:
    print("First if code block")
else:
    print("First Else code block")

if num1 ** num2 > 20:
    print("Second if code block")
else:
    print("Second Else code block")

if num1 ** num2 != 25:
    print("Third if code block")
else:
    print("Third Else code block")

myList = ["Aria", "Hunter", "Hannah", "Conner", "Eva", "Christian"]

for i in myList:
    print(i)
    print(len(myList))

counter = 3

while counter > 0:
    print("Countdown: ",counter)
    counter -= 1

print("Blast Off!")

x = 5
y = 6
z = 5 * 6
while True:
    

    if z > 90:
        break
    else:
        x = 10
        y = 12
        z = x * y

print(z)