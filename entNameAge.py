name = input("Enter your name: ")
age = -1

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("That wasn't an integer.")

print("Name: " + name)
print("Age: " + str(age))