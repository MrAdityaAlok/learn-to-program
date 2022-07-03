"""Solution to Ellen's Alien Game exercise."""


from typing import ClassVar, List, Tuple


class Alien:
    """Creates an Alien object with location x_coordinate and y_coordinate.

    Attributes:
        total_aliens_created: Total number of Aliens created so far.
        x_coordinate: Position on the x-axis.
        y_coordinate: Position on the y-axis.
        health: Amount of health points.
    """

    total_aliens_created: ClassVar[int] = 0

    def __init__(self, x_coordinate: int, y_coordinate: int) -> None:
        self.health = 3
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

        Alien.total_aliens_created += 1

    def hit(self) -> None:
        """Decrements Alien health by one point."""
        self.health = max(self.health - 1, 0)

    def is_alive(self) -> bool:
        """Checks if Alien is alive (i.e health is > 0)."""
        return self.health > 0

    def teleport(self, new_x_coordinate: int, new_y_coordinate: int) -> None:
        """Move Alien to a new location."""
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, _) -> None:
        """Implementation TBD."""


def new_aliens_collection(coordinates: List[Tuple[int, int]]) -> List[Alien]:
    """Creates and returns a list of Alien objects.

    Args:
        coordinates: list of coordinates for the Aliens.
    """
    return [Alien(*coordinate) for coordinate in coordinates]
