"""Functions to keep track and alter inventory."""


from typing import Dict, List, Tuple, Union


class Inventory(Dict):
    """A dictionary subclass similar to collections.Counter.

    Extra features:
        * It sets count to 0 if item is missing from inventory.
        * It ensures that no item's count is below 0.
    """

    def __missing__(self, _):
        return 0

    def __setitem__(self, k, v) -> None:
        return super().__setitem__(k, max(v, 0))


def create_inventory(items: List) -> Dict:
    """Create an inventory that tracks the amount of each `items` in list.

    Args:
        items: list of items to create an inventory from.

    Returns:
        the inventory dictionary.
    """
    inventory = Inventory()

    for item in items:
        inventory[item] += 1

    return inventory


def add_items(inventory: Dict, items: List) -> Dict:
    """Add or increment items count in inventory.

    Args:
        inventory: dictionary of existing inventory.
        items: list of items to update the inventory with.

    Returns:
        the inventory updated with the new items.
    """
    inventory = Inventory(inventory)

    for item in items:
        inventory[item] += 1

    return inventory


def decrement_items(inventory: Dict, items: List) -> Dict:
    """Decrement items in inventory using elements from the `items` list.

    Args:
        inventory: inventory dictionary.
        items: list of items to decrement from the inventory.

    Returns:
        updated inventory with items decremented.
    """
    inventory = Inventory(inventory)

    for item in items:
        inventory[item] -= 1

    return inventory


def remove_item(inventory: Dict, item: str) -> Dict:
    """Remove item from inventory if it matches `item` string.

    Args:
        inventory: inventory dictionary.
        item: item to remove from the inventory.

    Returns:
        updated inventory with item removed, or
        current inventory if item does not match.
    """
    if item in inventory:
        del inventory[item]

    return inventory


def list_inventory(inventory: Dict) -> Union[List, Tuple]:
    """Create a list containing all (item_name, item_count) pairs in inventory.

    Args:
        inventory: an inventory dictionary.

    Returns:
        list of (key, value) pairs from the inventory dictionary.
    """
    return [(item, count) for item, count in inventory.items() if count > 0]
