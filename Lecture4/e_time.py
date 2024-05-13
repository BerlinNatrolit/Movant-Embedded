# This is a short demo to demonstrate how much slower try-except is compared to if-statement.
import time

#exception
start = time.time_ns()
for i in range(10000):
    try:
        ans = int("f")
    except:
        pass

e = time.time_ns() - start
print(e)

############################
start = time.time_ns()
for i in range(180000):
    if not i:
        ans = 5
    else:
        pass

e = time.time_ns()-start
print(e)
