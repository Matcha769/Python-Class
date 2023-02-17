# Escape sequence = a combination of characters that has a meaning other than the literal characters


# Escape sequence
# \' : '
# \" : "
# \\ : \
# \n : new line
# \r : carriage return
# \t : tab
# \a : ring
# \b : backspace
# \x : hex
# \o : octal

str1 = "matcha said: \"Hi\""
print(str1)

str2 = "matcha\\"
print(str2)

str3 = "Hello\nMatcha"
print(str3)

str4 = "\tmatcha"
print(str4)

str5 = "M\batcha"
print(str5)

str6 = "he\rllo matcha"
str7 = "hello matc\rha"
print(str6)
print(str7)
