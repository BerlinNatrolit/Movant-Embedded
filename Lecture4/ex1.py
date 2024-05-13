numbers = [1,2,3,4,5,6,7]
print(f"The list of numbers is: {numbers}")

try:
    index = input("Write index: ")
    print(f"element at index {index} is {numbers[int(index)]}")
except:
    print("Exception")