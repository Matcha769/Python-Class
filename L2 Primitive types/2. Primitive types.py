# Primitive types = a set of basic data types from which all other data types are constructed.

# numeric type
    # integer (int)
    # floating point (float)
    # boolean (bool) (True / False) (except 0 are True) (0 False / 1 True)

int_num = 30
float_num = 34.35
flag = True

print(type(int_num))
print(type(float_num))
print(type(flag))

# num = int_num + flag
num = 30 + True
# num = 30 + 1 # 31

print(num)

num1 = 36.0
print(type(num1))
num2 = 36.
print(num2)

# Text sequence type
    # String (str)

str1 = "This is a string!"
print(str1)
str2 = 'This is a string too'
# str3 = "This is not valid' (bad)

str4 = "Matcha said: 'Hi'"
print(str4)