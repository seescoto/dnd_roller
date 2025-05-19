import random


def roll_custom(roll: str) -> int:
    """given a custom roll (ex. 1d10 +3, 2d20, d4) rolls the dice and adds any modifiers.
    string should be in the format [X]dY[+Z][-Z] where X,Y,Z are numbers and [] represents
    an optional addition to the string.
    e.g. "1d10 +3-4" "2d20-3" "d4"

    Args:
        roll (str): custom roll.

    Returns:
        int: result of dice roll plus or minus modifiers.
    """

    # pre-formatting
    roll = roll.lower()
    roll = roll.replace(" ", "")
    # if no prefix, is 1dX
    if roll[0] == "d":
        roll = "1" + roll

    # split into roll (XdY) and modifiers (+Z or -Z)
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


def compute_modifiers(modifier_string: str) -> int:

    if modifier_string == None:
        return 0
    modifier_string = "0" + modifier_string
    eq = eval(modifier_string)
    return eq


def roll_d4() -> int:
    return random.randint(1, 4)


def roll_d6() -> int:
    return random.randint(1, 6)


def roll_d8() -> int:
    return random.randint(1, 8)


def roll_d12() -> int:
    return random.randint(1, 12)


def roll_d20() -> int:
    return random.randint(1, 20)
