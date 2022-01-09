scores = {
    "AEIOULNRST": 1,
    "DG": 2,
    "BCMP": 3,
    "FHVWY": 4,
    "K": 5,
    "JX": 8,
    "QZ": 10,
}


def score(word: str):
    return sum(
        [
            value
            for letters, value in scores.items()
            for letter in word.upper()
            if letter in letters
        ]
    )


# Another implementation
#
# from enum import IntEnum
#
#
# class Scores(IntEnum):
#     A = E = I = O = U = L = N = R = S = T = 1
#     D = G = 2
#     B = C = M = P = 3
#     F = H = V = W = Y = 4
#     K = 5
#     J = X = 8
#     Q = Z = 10
#
#
# def score(word: str):
#     return sum([Scores[letter] for letter in word.upper()])
