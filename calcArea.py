def calculate_area(length, width):
    return length * width

length = float(input("What is the length? "))
width = float(input("What is the width? "))

area = calculate_area(length, width)
print(f"The area of the rectange is {area}")