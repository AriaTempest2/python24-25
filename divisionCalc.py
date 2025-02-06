numerator = int(input("Enter the Numerator: "))

try:
    denominator = int(input("Enter the Denominator: "))
    result = numerator / denominator
    print(f"The result is {result}")

except ZeroDivisionError:
    print("I HATE YOU!!!!!!")