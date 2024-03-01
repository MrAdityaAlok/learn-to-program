import random

ABILITIES = (
    "strength",
    "dexterity",
    "constitution",
    "intelligence",
    "wisdom",
    "charisma",
)


def modifier(constitution: int) -> int:
    return (constitution - 10) // 2


class Character:
    def __init__(self):
        for ability in ABILITIES:
            setattr(self, ability, self.ability())
        self.hitpoints: int = 10 + modifier(self.constitution)

    def ability(self) -> int:
        dice_rolls = tuple(random.randint(1, 6) for _ in range(4))
        return sum(dice_rolls) - min(dice_rolls)
