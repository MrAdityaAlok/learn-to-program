import random


class Robot:
    def __init__(self):
        """Manage robot factory settings."""
        self.__generate()

    def __generate(self):
        random.seed()
        self.name = "".join(
            random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 2)
        ) + str(random.randint(100, 999))

    def reset(self):
        self.__generate()
