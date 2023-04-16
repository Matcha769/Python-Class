# Operator
# Operand
# 2 + 3, operand1 operator operand2

# Unary Operator
# -3, +2

# Binary Operator
# +, -, *, / ....

5 + -3  # 2

# Assignment operator
a = 7
b = 18.5
print(id(a), id(b))

# Standard Swap
a, b = b, a
print(id(a), id(b))

# Arithmetic Operator
# +: addition
# -: substraction
# *: multiplication
# /: classic/ture division ----> always return float
# //: floor/integer division ----> return integer (except one or both of the operands are float)
# %: modulus
# **: exponentiation -----> read from right to left (right-sided)

x = 10

y = x + 1  # 11
y = x - 1  # 9
y = x * 5  # 50
y = x / 2  # 5.0
print(y)
y = x // 3  # 3
print(y)
y = x % 3  # 1
print(y)

print(2 ** 10)

print(2 ** 2 ** 3)  # 2 ** 8 = 256
print(2 ** (2 ** 3))  # 2 ** 8 = 256 (O)
print((2 ** 2) ** 3)  # 4 ** 3 = 64 (X)

# Compound Assignment Operator

x = 3
x = x + 2  # x += 2 (x = 5)
x = x - 2  # x -= 2 (x = 3)
x = x * 2  # x *= 2 (x = 6)
x = x / 2  # x /= 2 (x = 3.0)
x = x // 2  # x //= 2 (x = 1.0)
x = 10
x = x % 3  # x %= 3 (x = 1)
x = 2
x = x ** 3  # x **= 3 (x = 8)

# Relational Operator
x, y = 2, 3

x == y  # False
x != y  # True
x >= y  # False
x <= y  # True
x > y  # False
x < y  # True

# Logical Operator
# not
# and
# or
x, y = True, False

x and y  # False
x or y  # True
not x  # False
not y  # True

x, y = 2, 3
print(x >= y or x != y and x ** 2 > y)  # True

# Bitwise Operator
# & (and)
# | (or)
# ^ (Xor)
# ~ (not)

print(5 & 3)  # 1
'''
  0101 <--- 5 binary
& 0011 <--- 3 binary
--------------------
  0001 <--- 1 binary
'''
print(5 | 3)  # 7
'''
  0101 <--- 5 binary
| 0011 <--- 3 binary
--------------------
  0111 <--- 7 binary
'''
print(5 ^ 3)  # 6
'''
  0101 <--- 5 binary
^ 0011 <--- 3 binary
--------------------
  0110 <--- 6 binary
'''
print(~5)  # -6 (-(x + 1))
'''
  0101 <--- 5 binary
~
--------------------
  1010 <--- -6 binary
'''

# Bonus
# and, or
print(3 and 2 and 1)  # 1
print(3 and 0 and 2)  # 0
print(3 or 2 or 1)  # 3
print(0 or 2 or 3)  # 2

# Membership Operator
# in, not in
print("M" in "Matcha")
print("m" in "Matcha")
print("m" not in "Matcha")

# Identity Operator
# is, is not
x, y = 2.0, 2.0
print(id(x), id(y))
print(x is y, x == y)
z = 2
print(id(z))
print(x is z, x == z)

# Shift Operator
# >>, <<

print(6 >> 1)

'''
     0110 <--- 6 binary
>> 1
--------------------
     0011 <--- 3 binary
'''

print(6 << 1)

'''
     0110 <--- 6 binary
<< 1
--------------------
     1100 <--- 12 binary
'''

print(21 << 2)  # 21 * (2 ** 2) = 84
print(21 >> 3)  # 21 // (2 ** 3) = 2

'''
1. ()
2. **
3. Unary(+ , -) , not , ~
4. % , // , / , *
5. Binary(+ , -)
6. << , >>
7. & , | , ^
8. < , <= , > , >= , != , ==
9. = , +=  , -= , *= , /= , %= , <<= , >== , &= , ^=  , !=
10. in , not in , is , is not
11. and , or
'''
