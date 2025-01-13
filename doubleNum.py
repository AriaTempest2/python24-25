myNumbers = [2, 5, 12, 17, 25, 32]

def pow2(y):
    powOf2 = y ** 2
    return powOf2

for i in myNumbers:
    pow2(i)
    print(i, "to the power of 2 is", powOf2)

pow2(17)

print("Our function is complete")