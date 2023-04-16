# String slicing = creates a new substring from the source string and original string remains unchanged.
# indexed[] (subscript) [start:end:step]

name = "OG Matcha"

print(name[0])
print(name[-2])

print(name[0:2])
print(name[:2])
print(name[3:])
print(name[3:9])

cool_name = name[::2]
print(cool_name)
reverse_name = name[::-1]
print(reverse_name)

print(name)

website1 = "https://www.google.com"
website2 = "https://www.instagram.com"
website3 = "https://www.youtube.com"

index = slice(12, -4)

web1 = website1[index]
web2 = website2[index]
web3 = website3[index]

print(web1)
print(web2)
print(web3)