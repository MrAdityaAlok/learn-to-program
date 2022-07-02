"""Functions for compiling dishes and ingredients for a catering company."""


from typing import List, Set, Tuple, Union

from sets_categories_data import (
    ALCOHOLS,
    KETO,
    OMNIVORE,
    PALEO,
    SPECIAL_INGREDIENTS,
    VEGAN,
    VEGETARIAN,
)


def clean_ingredients(
    dish_name: str, dish_ingredients: List[str]
) -> Tuple[str, Set[str]]:
    """Remove duplicates from `dish_ingredients`.

    Args:
        dish_name: containing the dish name.
        dish_ingredients: list - dish ingredients.

    Returns:
        containing (dish_name, ingredient set).
    """
    return dish_name, set(dish_ingredients)


def check_drinks(drink_name: str, drink_ingredients: List[str]) -> str:
    """Classify drink type as "Cocktail" or "Mocktail.

    Classification is based on `drink_ingredients`. Drinks with alcoholic
    ingredients fall under "Cocktail" category otherwise is "Mocktail".

    Args:
        drink_name: name of the drink.
        drink_ingredients: ingredients in the drink.

    Returns:
        drink_name appended with "Mocktail" or "Cocktail".
    """
    return (
        f"{drink_name}"
        # If any dish ingredient is in ALCOHOLS then dish is an cocktail.
        f" {'Cocktail' if ALCOHOLS & set(drink_ingredients) else 'Mocktail'}"
    )


def categorize_dish(
    dish_name: str, dish_ingredients: List[str]
) -> Union[str, None]:
    """Categorize `dish_name` based on `dish_ingredients`.

    Args:
        dish_name: dish to be categorized.
        dish_ingredients: ingredients for the dish.

    Returns:
        the dish name appended with ": <CATEGORY>".
    """
    _dish_ingredients = set(dish_ingredients)

    for category, category_name in (
        (VEGAN, "VEGAN"),
        (VEGETARIAN, "VEGETARIAN"),
        (PALEO, "PALEO"),
        (OMNIVORE, "OMNIVORE"),
        (KETO, "KETO"),
    ):
        # Check if set dish_ingredients is subset of category set or not.
        if _dish_ingredients <= category:
            return f"{dish_name}: {category_name}"

    return None


def tag_special_ingredients(
    dish: Tuple[str, List[str]]
) -> Tuple[str, Set[str]]:
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`.

    Args:
        dish: of (dish name, list of dish ingredients).

    Returns:
        the dish name followed by the `set` of ingredients that require a
        special note on the dish description.
    """
    return (
        dish[0],
        # Extract ingredients common between dish[1] and SPECIAL_INGREDIENTS.
        set(dish[1]) & SPECIAL_INGREDIENTS,
    )


def compile_ingredients(dishes: List[Set[str]]) -> Set[str]:
    """Create a master list of ingredients.

    Args:
        dishes: of dish ingredient sets.

    Returns:
        ingredients compiled from `dishes`.
    """
    return set.union(*dishes)


def separate_appetizers(dishes: List[str], appetizers: List[str]) -> List[str]:
    """Determine which `dishes` are designated `appetizers` and remove them.

    Args:
        dishes: dish names.
        appetizers: appetizer names.

    Returns:
        dish names that do not appear on appetizer list.
    """
    return list(set(dishes) - set(appetizers))


def singleton_ingredients(
    dishes: List[Set[str]],
    intersection: Set[str],
) -> Set[str]:
    """Extract singleton ingredients from dishes.

    Args:
        dishes: ingredient sets.
        intersection: one of the `<CATEGORY>_INTERSECTION` constant.

    Returns:
        set containing singleton ingredients.
    """
    return set.union(*(dish - intersection for dish in dishes))
