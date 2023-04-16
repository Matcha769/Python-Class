# Format() = It formats the specified value(s) and insert them inside the string's placeholder.

age1 = 18
name1 = "Matcha"

# print("My name is %s, and I'm %d years old." %(name1, age1))
print("My name is {0}, and I'm {1} years old.".format(name1, age1))
print("My name is {1}, and I'm {0} years old.".format(age1, name1))

print("My name is {2}, and I'm {3} years old.".format(age1, name1, "Jack", 20))

print("My name is {name}, and I'm {age} years old.".format(name=name1, age=age1))

'''
s : string
i or d or u : decimal
b : binary  2 -> 10
o : octal
x : hex
f : float
e : scientific notation
'''

'''
< : left-side
> : right-side
^ : middle
0 : zero
#b : binary 2 -> 0b10
#o : octal
#x : hex
, : thousands separator
% : percentage
+ : add + before the value
'''

print("{}, {}".format(0.666, "matcha"))

print("{0:10}".format(0.666666))
print("{:10}".format("matcha"))
print("{0:<10}".format(0.666666))
print("{:>10}".format("matcha"))
print("{:^10}".format("matcha"))
print("{:^11}".format("matcha"))

print("{0:0^10}".format(0.666666))
print("{0:(^10}".format(0.666666))

print("{0:b}".format(10))
print("{0:#b}".format(10))

print("{:,}".format(1000 * 1000))


print("{0:.2%}".format(0.666666))
print("{0:.0%}".format(0.666666))

print("{0:+2}, {1:1}".format(18, 10))

print(format("Matcha", "^10"))
print(format(1234.456, "012,.2f"))
print("The " + format("money", "^10") + " is " + format(1234.456, "012,.2f") + " dollars.")

# f-string

print(f"The {'money':^10} is {1234.456:012,.2f} dollars.")

num1, num2 = 10, 15
print(f"{num1:^5} + {num2:^5} = {num1 + num2}")