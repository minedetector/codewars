def order_weight(strng):
    weight_sum = {}
    remember = []
    for i in strng.split():
        for x in i:
            remember.append(int(x))
        weight_sum[i] = sum(remember)
        del remember[:]
    weight_sum = sorted(weight_sum.items(), key=lambda val: val[1])

    return " ".join([y[0] for y in weight_sum])

print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))