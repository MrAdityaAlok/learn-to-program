"""Functions to manage and organize queues at Chaitana's roller coaster."""


from typing import List, Literal

# NOTE: Not using TypeAlias since it's only available in python>=3.10.
Queue = List[str]


def add_me_to_the_queue(
    express_queue: Queue,
    normal_queue: Queue,
    ticket_type: Literal[0, 1],
    person_name: str,
) -> Queue:
    """Add a person to the 'express' or 'normal' queue.

    Args:
        express_queue: names in the Fast-track queue.
        normal_queue: names in the normal queue.
        ticket_type: type of ticket. 1 = express, 0 = normal.
        person_name: name of person to add to a queue.

    Returns:
        the (updated) queue the name was added to.
    """
    if ticket_type == 0:
        normal_queue.append(person_name)
        return normal_queue

    express_queue.append(person_name)
    return express_queue


def find_my_friend(queue: Queue, friend_name: str) -> int:
    """Search the queue for a name and return their queue position (index).

    Args:
        queue: names in the queue.
        friend_name: name of friend to find.

    Returns:
        index at which the friends name was found.
    """
    return queue.index(friend_name)


def add_me_with_my_friends(
    queue: Queue, index: int, person_name: str
) -> Queue:
    """Insert the late arrival's name at a specific index of the queue.

    Args:
        queue: names in the queue.
        index: the index at which to add the new name.
        person_name: the name to add.

    Returns:
        queue updated with new name.
    """
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue: Queue, person_name: str) -> Queue:
    """Remove the mean person from the queue by the provided name.

    Args:
        queue: names in the queue.
        person_name: name of mean person.

    Returns:
        queue update with the mean persons name removed.
    """
    queue.remove(person_name)
    return queue


def how_many_namefellows(queue: Queue, person_name: str) -> int:
    """Count how many times the provided name appears in the queue.

    Args:
        queue: names in the queue.
        person_name: name you wish to count or track.

    Returns:
        the number of times the name appears in the queue.
    """
    return queue.count(person_name)


def remove_the_last_person(queue: Queue) -> str:
    """Remove the person at the last index in the queue and return their name.

    Args:
        queue: names in the queue.

    Returns:
        name that has been removed from the end of the queue.
    """
    return queue.pop()


def sorted_names(queue: Queue) -> Queue:
    """Sort names in the queue in alphabetical order and return the result.

    Args:
        queue: names in the queue.

    Returns:
        copy of the queue in alphabetical order.
    """
    queue.sort()
    return queue
