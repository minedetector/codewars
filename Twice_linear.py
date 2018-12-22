def dbl_linear(n):
    answer = 1
    y, z = [], []
    i = 0
    while True:
        if i >= n:
            return answer
        y.append(2 * answer + 1)
        z.append(3 * answer + 1)
        answer = min(y[0], z[0])

        if answer == y[0]:
            del y[0]
        if answer == z[0]:
            del z[0]

        i += 1

print(dbl_linear(20))
