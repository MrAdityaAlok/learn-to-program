def classify(num):
    if num < 1:
        raise ValueError("Given number is not a natural Number")
    _sum = sum(
        {
            fact  # starting from 2 as the num itself gets included when starring from 1(which not needed here)
            for i in range(2, int(num ** 0.5) + 1)
            if not num % i  # i.e if num % i == 0
            for fact in [i, num // i]
        }
    )
    _sum += 1 if num != 1 else 0  # adding 1 since started from 2
    return ("abundant", "perfect", "deficient")[
        2 if _sum < num else _sum == num
    ]
