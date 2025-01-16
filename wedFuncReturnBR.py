# def return_number(a, b):
#     return a + b

# result = add_numbers(5, 10)






# def calculate_area(radius):
#     new_radius = 3.14 * (radius ** 2)
#     return new_radius

# area = calculate_area(7)
# print("The area is", area)

def prod_subt(a, b):
    product = a * b
    difference = a - b
    return product, difference

prod, diff = prod_subt(8, 3)
print("product: ", prod)
print("Difference: ", diff)