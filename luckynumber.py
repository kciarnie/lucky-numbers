import click

__author__ = "Kevin Ciarniello"
__copyright__ = "Copyright 2017, Kevin Ciarniello"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Kevin Ciarniello"
__email__ = "kciarnie@gmail.com"

# Constants
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
LOWEST_NUMBER = 1
HIGHEST_NUMBER = 59
UNIQUE_NUMBER = 7
FEWEST_DIGITS = 7
MOST_DIGITS = 14


def is_valid(number):
    """
    This is a validation checker
    :param number: the input number to check
    :return: if the value is between 1 and 59
    """
    if isinstance(number, str):
        number = int(number)
    return LOWEST_NUMBER <= number <= HIGHEST_NUMBER


def left(i, valid_double_digits, entry, previous):
    if i + 1 < len(valid_double_digits) and valid_double_digits[i] and not valid_double_digits[i + 1]:

        # Pick entry 1 if it is not the same number as the previous value coming in
        if not entry[i] == previous:
            return entry[i]

    return None


def middle(i, valid_double_digits, entry, previous):
    if not valid_double_digits[i] and valid_double_digits[i + 1]:
        if not entry[i + 1] == previous:
            return entry[i + 1]
    return None


def right(i, valid_double_digits, entry, previous):
    if not valid_double_digits[i] and not valid_double_digits[i + 1]:
        right_digit = entry[i][1:]
        if not previous == right_digit:
            return right_digit


def display(original, result):
    if len(result) == UNIQUE_NUMBER:
        output = original + " -> "
        for value in result:
            output += " %s" % value
        print(output)


def double_parse(value):

    # Get all the potential double digits
    doubles = [value[i:i + 2] for i in range(0, len(value))]

    # Validate if they are between 1 and 59
    valid_digits = [is_valid(i) for i in doubles]

    result = {}
    previous = None
    for i, first_entry in enumerate(doubles):
        first = left(i, valid_digits, doubles, previous)
        second = middle(i, valid_digits, doubles, previous)
        third = right(i, valid_digits, doubles, previous)
        if first:
            result[i] = first
        elif second:
            result[i] = second
        elif third:
            result[i] = third

        if i in result:
            previous = result[i]

    # Convert to a list
    return [v for v in result.values()]


def single_parse(value):
    """
    Converts the string into a list of all the digits
    :param value: the input string 
    :return: a list of all the characters
    """
    return list(value)


def parse(value):
    """
    Parses through the string and gets a result of the potential string back
    :param value: 
    :return: 
    """

    if len(value) == UNIQUE_NUMBER:
        # If we are in this case, it's the unique situation that we only have 7 numbers in the string
        result = single_parse(value)
    else:
        # Every other situation and we are here
        result = double_parse(value)

    # Calls the display function
    display(value, result)


@click.command(short_help="Welcome to Uncle Morty's Lucky Numbers", context_settings=CONTEXT_SETTINGS)
def main():
    """
    Winning Ticket!

    Your favorite uncle, Morty, is crazy about the lottery and even crazier about how he picks his “lucky” numbers. 
    And even though his “never fail” strategy has yet to succeed, Uncle Morty doesn't let that get him down.

    Every week he searches through the Sunday newspaper to find a string of digits that might be potential lottery 
    picks. But this week the newspaper has moved to a new electronic format, and instead of a comfortable pile of 
    papers, Uncle Morty receives a text file with the stories.

    Help your Uncle find his lotto picks. Given a large series of number strings, return each that might be suitable 
    for a lottery ticket pick. Note that a valid lottery ticket must have 7 unique numbers between 1 and 59, digits 
    must be used in order, and every digit must be used.

    For example, given the following strings:

    [ "569815571556", “4938532894754”, “1234567”, “472844278465445”]

    Your function should return:

    4938532894754 -> 49 38 53 28 9 47 54
    1234567 -> 1 2 3 4 5 6 7
    """

    lists = ["569815571556", "4938532894754", "1234567", "472844278465445"]
    for digits in lists:
        if digits:
            length = len(digits)
            if FEWEST_DIGITS <= length <= MOST_DIGITS:
                parse(digits)


if __name__ == '__main__':
    main()
