import datetime
import random


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
    decimal = round(num - int(num), 2)
    if decimal == 0:
        decimal = "INTEGER"
    return decimal


# challenge 08
def fizzbuzz(num):
    result = num
    if (num % 3 == 0) and (num % 5 == 0):
        result = "FizzBuzz"
    elif num % 3 == 0:
        result = "Fizz"
    elif num % 5 == 0:
        result = "Buzz"
    return result


# challenge 09
def count_num_digits(input_string):
    count = 0
    for char in input_string:
        if char.isdigit():
            count += 1
    return count


# challenge 10
def sum_pos_divisor(num):
    sum_of_divisors = 0
    for i in range(1, num - 1):
        if (num % i) == 0:
            sum_of_divisors += i
    return sum_of_divisors == num


# challenge 11
def check_friday_13(yr, mon):
    date = datetime.date(yr, mon, 13)
    return date, date.weekday() == 4


# challenge 12
def check_division(a, b):
    num = a + 1
    while num % b != 0:
        num += 1
    return num


# challenge 13
def calculate_length():
    count = 0
    n = random.randint(1, 5000)
    num = n
    while num > 0:
        count += 1
        num //= 10
    return n, count


# challenge 14
def booleans(x, y, z):
    result = False
    if x & y:
        result = True
    elif x & z:
        result = True
    elif z & y:
        result = True
    return x, y, z, result
