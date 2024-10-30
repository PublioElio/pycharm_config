def sum_num(a, b, c):
    total = (a + b + c)
    if a == b == c:
        total *= 2
    return total


def sqrt(num):
    estimation = num / 2.0
    tolerance = 0.00001
    while abs(estimation * estimation - num) > tolerance:
        estimation = (estimation + num / estimation) / 2.0
    return round(estimation, 3)
