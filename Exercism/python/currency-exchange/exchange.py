"""Module implementing currency exchange functions."""


def _actual_exchange_rate(exchange_rate: float, spread: int) -> float:
    return exchange_rate + exchange_rate * spread / 100


def exchange_money(budget: float, exchange_rate: float) -> float:
    """Calculates exchange value of foreign currency.

    Args:
        budget: amount of money you are planning to exchange.
        exchange_rate: unit value of the foreign currency.

    Returns:
        exchanged value of the foreign currency you can receive.
    """
    return budget / exchange_rate


def get_change(budget: float, exchanging_value: int) -> float:
    """Calculates amount of money left after exchanging currency.

    Args:
        budget: amount of money you own.
        exchanging_value: amount of your money you want to exchange now.

    Returns:
        amount left of your starting currency after exchanging.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """Calculates total value of bills.

    Args:
        denomination: the value of a bill.
        number_of_bills: amount of bills you received.

    Returns:
        total value of bills you now have.
    """
    return denomination * number_of_bills


def get_number_of_bills(budget: float, denomination: int) -> int:
    """Calculates number of bills you have to pay.

    Args:
        budget: the amount of money you are planning to exchange.
        denomination: the value of a single bill.

    Returns:
        number of bills after exchanging all your money.
    """
    return int(budget // denomination)


def exchangeable_value(
    budget: float, exchange_rate: float, spread: int, denomination: int
) -> int:
    """Calculates exchangeable value.

    Args:
        budget: the amount of your money you are planning to exchange.
        exchange_rate: the unit value of the foreign currency.
        spread: percentage that is taken as an exchange fee.
        denomination: the value of a single bill.

    Returns:
        maximum value you can get.
    """
    return (
        get_number_of_bills(
            exchange_money(
                budget, _actual_exchange_rate(exchange_rate, spread)
            ),
            denomination,
        )
        * denomination
    )


def non_exchangeable_value(
    budget: float, exchange_rate: float, spread: int, denomination: int
) -> int:
    """Calculates non-exchangeable value.

    Args:
        budget: the amount of your money you are planning to exchange.
        exchange_rate: the unit value of the foreign currency.
        spread: percentage that is taken as an exchange fee.
        denomination: the value of a single bill.

    Returns:
        non-exchangeable value.
    """
    return int(
        exchange_money(budget, _actual_exchange_rate(exchange_rate, spread))
        - exchangeable_value(budget, exchange_rate, spread, denomination)
    )
