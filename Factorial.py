def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# test the factorial function
print(factorial(5))
print(factorial(0))
print(factorial(1))
print(factorial(2))
