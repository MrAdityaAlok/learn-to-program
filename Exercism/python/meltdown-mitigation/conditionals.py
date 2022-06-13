"""Functions to prevent a nuclear meltdown."""


from typing import Literal, Union


def is_criticality_balanced(
    temperature: Union[int, float], neutrons_emitted: Union[int, float]
) -> bool:
    """Verify criticality is balanced.

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.

    Args:
        temperature: temperature value in kelvin.
        neutrons_emitted: number of neutrons emitted per second.

    Returns:
        is criticality balanced?
    """

    return (
        temperature < 800
        and neutrons_emitted > 500
        and temperature * neutrons_emitted < 500000
    )


def reactor_efficiency(
    voltage: Union[int, float],
    current: Union[int, float],
    theoretical_max_power: Union[int, float],
) -> Literal["green", "orange", "red", "black"]:
    """Assess reactor efficiency zone.

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as:
        (generated power/ theoretical max power)*100
    where generated power = voltage * current

    Args:
        voltage: voltage value.
        current: current value.
        theoretical_max_power: power that corresponds to a 100% efficiency.

    Returns:
        color representing efficiency of reactor.
    """
    efficiency = ((voltage * current) / theoretical_max_power) * 100
    color = "black"  # Default for efficiency < 30.

    if efficiency >= 80:
        color = "green"
    elif efficiency >= 60:
        color = "orange"
    elif efficiency >= 30:
        color = "red"

    return color


def fail_safe(
    temperature: Union[int, float],
    neutrons_produced_per_second: Union[int, float],
    threshold: Union[int, float],
) -> Literal["LOW", "NORMAL", "DANGER"]:
    """Assess and return status code for the reactor.

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` within +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges

    Args:
        temperature: value of the temperature in kelvin.
        neutrons_produced_per_second: neutron flux.
        threshold: threshold for category.
    """
    product = temperature * neutrons_produced_per_second

    status_code = "DANGER"
    if product < 0.9 * threshold:
        status_code = "LOW"

    if threshold - 0.1 * threshold < product < 0.1 * threshold + threshold:
        status_code = "NORMAL"

    return status_code
