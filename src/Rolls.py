import random
import math


def roll_custom(roll: str):

    # roll string in the format NUMdNUM +/- NUM
    # ex "1d10+3" or "d20 - 4" or "1d8"

    # pre-formatting
    roll = roll.lower()
    roll = roll.replace(" ", "")
    # if no prefix, is 1dX
    if roll[0] == "d":
        roll = "1" + roll

    # split into roll (xdx) and modifiers (+x-y)
    strings = split_by_multiple(roll, ['-', '+'])
    mods = compute_modifiers(strings[1])

    # roll dice
    roll = strings[0].split("d")
    dice = 0
    for _ in range(int(roll[0])):
        dice += random.randint(1, int(roll[1]))

    return dice + mods


def split_by_multiple(string: str, deliminators: list[chr]) -> tuple[str]:
    """split a string into 2 parts by any of multiple deliminators.
    if deliminators are not present, return (string, None))

    Args:
        string (str): string to split
        deliminators (list[chr]): list of characters to split by

    Returns:
        strings (tuple[str]): string split into 2 by deliminators,
        keeping the deliminators in the second half of the split
    """

    for i in range(len(string)):
        if string[i] in deliminators:
            return (string[0:i], string[i:])

    return (string, None)


def compute_modifiers(modifier_string: str):
    if modifier_string == None:
        return 0
    modifier_string = "0" + modifier_string
    eq = eval(modifier_string)
    return eq


print(roll_custom("1d1"))
# print(compute_modifiers("+2+4+5"))
