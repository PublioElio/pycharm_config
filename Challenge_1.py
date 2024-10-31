# challenge 01
def sum_num(a, b, c):
    total = (a + b + c)
    if a == b == c:
        total *= 2
    return total


# challenge 02
def sqrt(num):
    estimation = num / 2.0
    while abs(estimation * estimation - num) > 0.00001:
        estimation = (estimation + num / estimation) / 2.0
    return round(estimation, 3)


# challenge 03
def quot_rem(num1, num2):
    return round(num1 / num2, 2), num1 % num2


# challenge 04
def even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"


# challenge 05
def factors(number):
    factors_list = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors_list.append(i)
    return factors_list


# challenge 06
def power(x, y):
    result = 1
    for i in range(y):
        result *= x
    return result


# challenge 07
def decimal_part(num):
    result = 0
    
    return result
