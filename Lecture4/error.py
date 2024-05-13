# creating our own exception by extending ValueError.
class InputValueError(ValueError):
    # Some input is wrong.
    pass

# Here we can force a divide by zero-exception.
def divide_hundred_by(a):
    return 100/a

print("Hello world!")
# prin("this is an error")          # syntax error, prin does not exist. should be print.
print(divide_hundred_by(5))
# print(divide_hundred_by(0))       # runtime error

# another runtime error. A pure bug. wrong numbers are given.
print([x for x in range(10)])       # print all numbers from 1 to 10

# Try except.
try:                                                                # lets try something
    t = int(input("Ange täljare: "))
    n = int(input("ange nämnare: "))
    ans = t/n
except (ValueError, ZeroDivisionError):                             # Oh no, we got an exception
    print("You did not give correct values.")
    raise ValueError("Wrong error was given as input.")             # we want to raise the exception we created earlier.
except RuntimeError as e:                                           # antoher exception.
    print("This is a runtime error")
else:                                                               # if we dont get an exception, this is what will be run.
    print(f"There was no exception!!!! So we have an answer{ans}")
finally:                                                            # and finally, always run this.
    print("This is a final statement! and will always be run")


# Please dont do this!
# If-statement is the proper way
while True:
    try:
        x = int(input("Give a number please: "))
        print(f"You wrote {x}")
    except ValueError:
        print("That was not a number, please give a true number!!!")