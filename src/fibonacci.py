def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("N:"))
print(fibonacci(n+1))