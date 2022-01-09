from math import log10


def is_armstrong_number(number):
    num = number
    exponent = int(log10(num)) + 1 if num != 0 else 0
    _sum = 0
    while num != 0:
        _sum += pow(num % 10, exponent)
        num = num // 10
    return _sum == number
