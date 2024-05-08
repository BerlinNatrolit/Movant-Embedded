import math

# Variable length arguments, can be any number of arguments and are named with a *.
def func(*args):
    for arg in args:
        print(arg)
    return ("value1", "value2")

# **arguments is a key word argument.
def func2(arg1, arg2, *args, **arguments):
    print(arg1)
    print(args)
    print(arguments["location"])

# Print function uses variable length arguments.
print(45)
print("Hello world")
print("hello ", 45, 45, 46, 47, 48, 48)

# Calling function with variable length arguments.
v1 = func(2, 3, "morot", "bil", "häst", 3.14159, math.pi)
print(v1)

# first two are positional arguments (ordinary arguments)
# the next two are variable length arguments,
# the last three are key word arguments.
func2(45, 24, 25, 26, action="hello", location="world", importance="!")