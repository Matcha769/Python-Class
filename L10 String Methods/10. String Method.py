# String methods

s1 = "hello World!"

print(s1.capitalize())
# s2 = s1.capitalize()
# print(s2)
print(s1.upper())
print(s1.lower())
# print(s1.casefold())
print(s1.title())
print(s1.swapcase())

print(s1.center(20, "0"))
print(s1.rjust(20, "0"))
print(s1.ljust(20, "0"))

print("  mmm   aaa  ".strip())
print("  mmm   aaa  ".rstrip())
print("  mmm   aaa  ".lstrip())

print(s1.replace("l", "e", 2))
print("  mmm   aaa  ".replace(" ", ""))

s2 = "Matcha code!"

print(s2.find("a", 4, 6))
# print(s2.index("a", 6))

print(s2.count("a"))
print(s2.count("m"))

print(s2.startswith("m"))
print(s2.endswith("!"))

print(s2.isalnum())
print(s2.isalpha())


print('42'.isdecimal())        # True
print('42'.isdigit())          # True
print('42'.isnumeric())        # True

print('42.5'.isdecimal())        # False
print('42.5'.isdigit())          # False
print('42.5'.isnumeric())        # False

print('\u00b2'.isdecimal())    # False
print('\u00b2'.isdigit())      # True
print('\u00b2'.isnumeric())    # True

print('\u2153'.isdecimal())    # False
print('\u2153'.isdigit())      # False
print('\u2153'.isnumeric())    # True

# isnumeric() > isdigit() > isdecimal()

print(s2.isupper())
print(s2.islower())

print("MATCHA!!".isupper())

print(max(s2))
print(min(s2))
print(min("Azi"))

print(len(s2))
