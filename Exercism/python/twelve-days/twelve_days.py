gifts = [
    ("On the {} day of Christmas my true love gave to me: {}"),
    ("first", "a Partridge in a Pear Tree"),
    ("second", "two Turtle Doves"),
    ("third", "three French Hens"),
    ("fourth", "four Calling Birds"),
    ("fifth", "five Gold Rings"),
    ("sixth", "six Geese-a-Laying"),
    ("seventh", "seven Swans-a-Swimming"),
    ("eighth", "eight Maids-a-Milking"),
    ("ninth", "nine Ladies Dancing"),
    ("tenth", "ten Lords-a-Leaping"),
    ("eleventh", "eleven Pipers Piping"),
    ("twelfth", "twelve Drummers Drumming"),
]


def recite(start_verse, end_verse):
    return [
        gifts[0].format(
            gifts[n][0],
            f"{', '.join(gifts[day][1] for day in range(n, 1, -1))}{('',', and ')[n>1]}{gifts[1][1]}.",
        )
        for n in range(start_verse, end_verse + 1)
    ]


# NOTE for myself:
# tuple and gifts[1][1] is just to not commit 'so called cheating in lyrics'
