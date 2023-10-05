#!/usr/bin/python3
"""
a method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Args: list of list representing boxes
    Return: True if all boxes can be opened else false
    """
    keys_gotten = []
    j = len(boxes)

    """check if a box is empty and not the last in sequence"""
    for box in boxes:
        if len(box) == 0 and box is not boxes[j-1]:
            return False
        """Append collected keys from an opened box in  a list"""
        for k in box:
            keys_gotten.append(k)

    """Check if a box has a matching key in the collected keys"""
    for index, keys in enumerate(boxes):
        if index in keys_gotten or index < j-1:
            return True
        else:
            return False
