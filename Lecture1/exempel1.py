# This is a comment
# this is line 2
# this is line 3
# this is line 4
tal = 3.14159           # variabler behöver inte 
print(tal)
print(type(tal))
print("Pi is: ", tal)   # one way to print variables
print("Pi is: " + str(tal))   # another way to do it

'''
This is a multi line string
this can be used as a complement
to the nonexistent multiline comment
'''

integer = 6
print(integer)
print(type(integer))

string = "Hello everyone"
print(string)
print(type(string))

string = 7
print(type(string))

number = "154"
print(number)
print(type(number))

print(2**4)
print("\n\n")

# strängar och index.
s = "Simon är full med frågor, sköj!!!"
print(s)        # whole string
print(s[6])     # 6th letter in string
print(s[:6])    # all letters before 6th letter
print(s[6:])    # all letters after 6th letter
print(s[:6] + s[7:])    #all letters except 6th
s = s[:6] + s[7:]   # save them again
print(s[-7])        # 7th letter from the back
print(s[-3:])       # the last three letters
print(s[:-3])       # all letters except last three
print(s[::1])   # every item in string
print(s[::2])   # every other item in string
print(s[::3])   # every third item in string
###########################################################

#user input
ans = input("Vad heter du: ")
print("Hej " + ans)

# if statement
# tänk på att det är indenteringen som avgör vad som hör till if-satsen.
num = 3

if num > 0:
    print("The number is positive!")
elif num < 0:
    print("this is a negative number")
else:
    print("we are now in the else statement from the first if statement.")

print("we are now outside of if")

# for loop
for i in range(3,10,2):
    print(i)

    for j in range(10,2,-3):
        print(j)
print("\n\n")

# loopa över en lista?
string = "Hello"
# the C -way
for i in range(0,len(string),1):
    print(string[i] + "-")

# the python way - for each
for letter in string:
    print(letter + "-")

# lite mer strängfunktioner.
str1 = "Hello"
str2 = "hello"
print(str1 == str2)
print(str1.islower())
print(str1.upper())
print(len(str1))

print(len(str1) == 5)

#for loop med range
j=0
for i in range(1,10):
    j = j + 1
    print(j)

# while emulation of do-while
run = True  # boolean in python is True and False, not true and false
while run:
    j = j+1
    print("while loop: ", j)

    if(j> 10):
        run = False

# lists
colors = ["red","blue","green"]
numbers = [1,2,3,4,5,6,7,8]

numbers1 = [1,2,3,4]
numbers2 = [5,6,7,8]
numbers = numbers + numbers2
print(numbers)

for i in numbers:
    s = i+3
    print(str(s))

print(len(numbers))

print(colors)
colors += ["orange"]
print(colors)
colors.append("yellow")
print(colors)
colors.insert(0, "magenta")
print(colors)
colors.remove("orange")
print(colors)
colors.pop(2)
print(colors)
color = sorted(colors)
print(colors)

# tuples
tuple = (1,2,3,4)
tuple = (5,6,7,8)
print(tuple)

# random, and import. Imports are usually done in the beginning.
import random

value = random.randint(0,10)
print(value)