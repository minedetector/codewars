from numpy import prod


def persistence(n):
    count = 1
    result = str(prod([int(i) for i in str(n)]))
    while True:
        if int(result) < 10:
            return count if count > 1 else 0
        result = str(prod([int(i) for i in result]))
        count += 1


print(persistence(412601))
