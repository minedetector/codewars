from fractions import Fraction


def convertFracts(lst):
    denom_sum = str(sum(Fraction(x[0], x[1]) for x in lst))
    #  If all numbers have a denominator of 1 then return original list
    try:
        if int(denom_sum):
            return lst
    except ValueError:
        pass
    denominator = int(denom_sum[denom_sum.find("/") + 1:])

    output = [[int((denominator/i[1])*i[0]), denominator] for i in lst]

    return output

a = [[1, 2], [1, 3], [1, 4]]
print(convertFracts(a))