# Print = prints the values to a stream

print("Hello")

print(100, "Have fun", True)
print(100, "Have fun", True, sep=" ")

print(100, "Have fun", True, end="777")
print("Test")
print("Test2")

'''
%d : int
%f : float
%s : string
%e & %E : scientific notation
%% : percent
'''

name = "Matcha"
age = 18
height = 183.56789

print("Hi, I'm %s, I'm %d years old and %f centimeter tall" %
      (name, age, height))
print("Hi, I'm %10s, I'm %5d years old and %f centimeter tall" %
      (name, age, height))
print("Hi, I'm %5s, I'm %d years old and %f centimeter tall" %
      (name, age, height))
print("Hi, I'm %s, I'm %d years old and %10.3f centimeter tall" %
      (name, age, height))
print("Hi, I'm %-10s, I'm %d years old and %10.3f centimeter tall" %
      (name, age, height))

print("%.2e" % (height))
print("The percent is %f %%" % (height))
