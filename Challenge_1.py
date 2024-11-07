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
    result = (x and y) or (x and z) or (y and z)
    return x, y, z, result


# challenge 15
def factorial():
    num = random.randint(1, 10)
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return num, fact


# challenge 16
def check_division_two(num):
    return num, num % 1 == 0


# challenge 17
def prime_num(num):
    is_prime = False
    if num > 1:
        is_prime = True
        count = 2
        num_sqrt = int(num ** 0.5)
        while count <= num_sqrt and is_prime:
            is_prime = num % count != 0
            count += 1
    return is_prime


# challenge 18
def sum_digits():
    n = random.randint(100, 300)
    total = sum_digits_of_number(n)
    return n, total


def sum_digits_of_number(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total


# challenge 19
def divide_by_15():
    input_list = generate_list(10)
    return input_list, get_divisible_by_15(input_list)


def generate_list(length):
    return [random.randint(0, 100) for _ in range(length)]


def get_divisible_by_15(input_list):
    return [number for number in input_list if number % 15 == 0]


# challenge 20
def swap_bits(num):
    binary_str = f'{num:08b}'
    pos1, pos2 = 2, 6
    binary_list = list(binary_str)
    binary_list[pos1], binary_list[pos2] = binary_list[pos2], binary_list[pos1]
    swapped_binary_str = ''.join(binary_list)
    return int(swapped_binary_str, 2)


# challenge 21
def fibonacci():
    n = random.randint(5, 10)
    output_sequence = [0, 1, 1, 2, 3]
    while len(output_sequence) < n:
        next_number = output_sequence[-1] + output_sequence[-2]
        output_sequence.append(next_number)
    return n, output_sequence


# challenge 22
def string_reverse(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name[::-1]


# challenge 23
def swap_strings(s1, s2):
    s1, s2 = s2, s1
    return s1, s2


# challenge 24
def count_vowels(input_string):
    # Un conjunto (set) es más eficiente para las comprobaciones de pertenencia que una cadena.
    vowels_set = {'a', 'e', 'i', 'o', 'u'}
    vowels = 0
    for char in input_string.lower():
        if char in vowels_set:
            vowels += 1
    return vowels


# challenge 25
def remove_duplicates(input_string):
    seen = set()
    output_string = []
    for char in input_string:
        if char not in seen:
            seen.add(char)
            output_string.append(char)
    return ''.join(output_string)


# challenge 26
def remove_consecutive_duplicates(input_string):
    if not input_string:
        output_string = ""
    else:
        output_string = [input_string[0]]
        for char in input_string[1:]:
            if char != output_string[-1]:
                output_string.append(char)
        output_string = "".join(output_string)
    return output_string


# challenge 27
def reverse_string(input_string):
    string_list = input_string.split()
    string_list.reverse()
    return " ".join(string_list)


# challenge 28
def longest_prefix(s1, s2, s3, s4):
    shortest_str = min(s1, s2, s3, s4, key=len)
    count = 0
    mismatch_found = False
    while count < len(shortest_str) and mismatch_found == False:
        if s1[count] != s2[count] or s2[count] != s3[count] or s3[count] != s4[count]:
            shortest_str = shortest_str[:count]
            mismatch_found = True
        count += 1
    return shortest_str


# challenge 29
def new_letter(s, t):
    correct_word = set(s)
    extra_letter = None
    for char in t:
        if char not in correct_word:
            extra_letter = char
            break
    return extra_letter


# challenge 30
def string_to_bool(input_string):
    output = "Invalid input"
    if input_string.lower() == 'true':
        output = True
    elif input_string.lower() == 'false':
        output = False
    return output


# challenge 31
def remove_spaces(input_string):
    return ''.join([char for char in input_string if char != ' '])


# challenge 32
def str_to_int(input_string):
    i = input_string.find('.')
    if i != -1:
        input_string = input_string[:i]
    return int(input_string)


# challenge 33
def copies_of_string(input_string, num):
    return input_string * num


# challenge 34
def count_case(sample_string):
    return sum(1 for char in sample_string if char.isupper())
