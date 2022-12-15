# Type casting = converting one datatype into another (type-conversion)

# Implicit Type Conversion
    # bool ---> int ---> float
    # small ------------ large

num1 = True + 35
print(num1)
num2 = 35 + 11.0
print(num2)

# Explicit Type Conversion
    # int()
    # float()
    # str()
    # bool()

num3 = 23 + int("73")
print(num3)
num4 = 1 + int(9.28) # 1 + 9
print(num4)
num5 = bool(5)
num6 = bool(0)
print(num5)
print(num6)

print(bool(10))
print(bool(0))
print(bool(0.0))
print(bool("A stirng"))
print(bool(""))
print(10 + "day")