def fibonacci(n, cache={}):
    value = 0
    if n in cache:
        return cache[n]
    if n <= 0:
        return 0
    if n == 1:
        return 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n - 1) + fibonacci(n - 2)

    cache[n] = value

    return value

print(fibonacci(70))