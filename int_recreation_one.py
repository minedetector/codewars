from math import sqrt


def list_squared(m, n):
    cache = []
    output = []

    for i in range(m, n + 1):
        if i == 1:
            output.append([1, 1])
            continue
        cache.append(i)
        cache.append(1)
        if i % 2 == 0:
            if i % 2 == 0 and i / 2 not in cache:
                cache.append(i / 2)
            if i % 3 == 0 and i / 3 not in cache:
                cache.append(i / 3)
            if i % 4 == 0 and i / 4 not in cache:
                cache.append(i / 4)
            for x in range(2, i // 4):
                if i % x == 0:
                    cache.append(x)
        else:
            for y in range(2, i // 3 + 1):
                if i % y == 0:
                    cache.append(y)
        z = sum(a ** 2 for a in cache)
        if sqrt(z) == int(sqrt(z)):
            output.append([i, z])
        del cache[:]
    return output


print(list_squared(1, 250))

"""
#  Best solution on net, dont know how cache works
CACHE = {}

def squared_cache(number):
    if number not in CACHE:
        divisors = [x for x in range(1, number + 1) if number % x == 0]
        CACHE[number] = sum([x * x for x in divisors])
        return CACHE[number] 
    
    return CACHE[number]

def list_squared(m, n):
    ret = []

    for number in range(m, n + 1):
        divisors_sum = squared_cache(number)
        if (divisors_sum ** 0.5).is_integer():
            ret.append([number, divisors_sum])

    return ret"""