"""This module implements a clock that handles time without date.

It is able to add and subtract minutes from given time, can also
check for equality of clocks that represent same time.

Examples:
    >> x = Clock(1,20)
    >> print(x)
    01:20
    >> print(x.hours)
    1
    >> print(x.minutes)
    20
    >> print(x.time_in_minutes) # minutes passed since 00:00 (midnight)
    80
    >> print(x + 56)
    02:16
    >> print(x - 56)
    00:24
    >> y = Clock(1,20)
    >> print(x==y) # both represents equal time
    True

    >> z = Clock(-1,-20)
    >> # negative time represents amount of time behind midnight (00:00)
    >> # here 80 (1 * 60 + 20) minutes behind midnight.
    >> print(z)
    'Clock(22, 40)'
"""


class Clock:
    """Represents a clock that handles time without date.

    Attributes:
        hours: represents hours passed since midnight.
        minutes: represents minutes passed.
        time_in_minutes: represents time in minutes passed since
            midnight.
    """

    def __init__(self, hour: int, minute: int) -> None:
        """Initialize clock.

        Args:
            hour: hours passed since midnight.
            minute: minute passed.
        """
        self._wrap(hour * 60 + minute)

    def _wrap(self, total_minutes: int) -> None:
        self.time_in_minutes: int = (
            total_minutes // 60 % 24
        ) * 60 + total_minutes % 60

    def __repr__(self):
        return (
            f"Clock({self.time_in_minutes // 60 % 24},"
            f" {self.time_in_minutes % 60})"
        )

    def __str__(self) -> str:
        return "{:02d}:{:02d}".format(
            self.time_in_minutes // 60 % 24,
            self.time_in_minutes % 60,
        )

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, Clock)
            and other.time_in_minutes == self.time_in_minutes
        )

    def __add__(self, minutes):
        return Clock(hour=0, minute=self.time_in_minutes + minutes)

    def __sub__(self, minutes):
        return Clock(hour=0, minute=self.time_in_minutes - minutes)
