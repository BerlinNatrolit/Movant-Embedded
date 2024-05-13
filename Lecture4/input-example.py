# short example of an input statement with an if-statement rather than try-except.
ans = 0
while True:
    ans = input("please write a number: ")
    if ans.isdigit():
        ans = int(ans)
        break

print(f"you wrote: {ans}")