# Create a function with two positional arguments.
def addition(a, b):
    sum = a+(-b)
    if sum > 0:
        return sum		# we dont need to define return value, or even have return value on all paths in the funciton/method.
    
def multiplication(a, b):
    prod = a*b
    return prod
    
def something_else(a,b):
    something = a**b
    return something

# Lets call some functions.
sum = addition(4,5)
prod = multiplication(4,5)
x = something_else(4,5)
print(f"Hello everyone them sum is: {sum}, prod is {prod}, and somethign else {x}")