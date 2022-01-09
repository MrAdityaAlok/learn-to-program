from math import ceil


def factors(value):
    prime_factors, n = [], value
    for i in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
        while n % i == 0:
            prime_factors.append(i)
            n //= i

    increments, i = [4, 2, 4, 2, 4, 6, 2, 6], 0
    for d in range(37, ceil(n ** 0.5) + 1):
        while n % d == 0:
            prime_factors.append(d)
            n //= d
        if i == 8:
            i = 0
        d += increments[i]

    if n > 1:
        prime_factors.append(n)

    return prime_factors
