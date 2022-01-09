RAIN_SOUNDS = {
    3: "Pling",
    5: "Plang",
    7: "Plong",
}


def convert(number):
    sounds = "".join(
        sound for factor, sound in RAIN_SOUNDS.items() if not number % factor
    )
    # if sounds is not empty or None, the left hand side is executed
    return sounds or str(number)
