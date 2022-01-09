from itertools import product


def is_triangle(sides) -> bool:
    return all(sum(pair[:2]) >= pair[2] != 0 for pair in product(sides, repeat=3))


def equilateral(sides):
    return is_triangle(sides) and sides[0] == sides[1] == sides[2]


def isosceles(sides):
    return is_triangle(sides) and (
        sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]
    )


def scalene(sides):
    return is_triangle(sides) and sides[0] != sides[1] != sides[2]
