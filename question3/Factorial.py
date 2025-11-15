def factorial(n):
    factorial = 1
    for i in range(n):
        factorial *= i+1

    return factorial
n = 5
print(factorial(n))