from datetime import timedelta


def add(moment):
    """Add a gigasecond (10**9 seconds) to given moment.

    Args:
        moment (datetime.datetime): momemt to which gigasecond is to be added.

    Returns:
        datetime.datetime: given moment with a gigasecond added to it.
    """
    gigasecond = timedelta(seconds=10**9)
    return moment + gigasecond
