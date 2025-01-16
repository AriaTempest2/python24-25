def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return 

print("1. Convert Celsius to Fahrenheit")
print("2. Convert Fahrenheit to Celsius")
choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"{celsius}° Celsius is equal to {celsius_to_fahrenheit(celsius):.2f}")
elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(f"{fahrenheit}° Fahrenheit is equal to {fahrenheit_to_celsius(fahrenheit):.2f}")
else:
    print("Invalid Choice!")