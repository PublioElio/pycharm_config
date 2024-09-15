def sum_num(a, b, c):
    total = (a + b + c)
    if a == b == c:
        total *= 2
    return total


def sqrt(num):
    estimation = num / 2.0
    while abs(estimation * estimation - num) > 0.00001:
        estimation = (estimation + num / estimation) / 2.0
    return round(estimation, 3)


def quot_rem(num1, num2):
    return round(num1 / num2, 2), num1 % num2


def even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"
