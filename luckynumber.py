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
    # Check to see if the number is a str
    if isinstance(number, str):
        # If so, we convert it to an integer and check if it is between 1 and 59
        number = int(number)

    return LOWEST_NUMBER <= number <= HIGHEST_NUMBER


def left(i, valid_digits, entries, previous_entry):
    if i + 1 < len(valid_digits) and valid_digits[i] and not valid_digits[i + 1]:

        # Pick entry 1 if it is not the same number as the previous value coming in
        current_entry = entries[i]
        if not current_entry == previous_entry:
            return current_entry

    return None


def middle(i, valid_digits, entries, previous_entry):
    if not valid_digits[i] and valid_digits[i + 1]:
        next_entry = entries[i + 1]
        if not next_entry == previous_entry:
            return next_entry
    return None


def right(i, valid_digits, entry, previous_entry):
    if not valid_digits[i] and not valid_digits[i + 1]:
        right_digit = entry[i][1:]
        if not previous_entry == right_digit:
            return right_digit


def display(initial_value, result):
    """
    This is the display function
    ex. 4938532894754 -> 49 38 53 28 9 47 54
    :param initial_value: the initial string of digits, ie 1234567 or 4938532894754
    :param result: The resulting list of values that should correspond to what should be outputted
    :return: prints the output if the values are the proper 7 unique digits between 1 and 59
    """
    if len(result) == UNIQUE_NUMBER:
        output = initial_value + " -> "
        for value in result:
            output += " %s" % value
        print(output)


def double_parse(value):
    # Get all the potential double digits
    doubles = [value[i:i + 2] for i in range(0, len(value))]

    # Validate if they are between 1 and 59
    valid_digits = [is_valid(i) for i in doubles]

    result = {}
    previous_entry = None
    for i, first_entry in enumerate(doubles):
        first = left(i, valid_digits, doubles, previous_entry)
        second = middle(i, valid_digits, doubles, previous_entry)
        third = right(i, valid_digits, doubles, previous_entry)
        if first:
            result[i] = first
        elif second:
            result[i] = second
        elif third:
            result[i] = third

        if i in result:
            previous_entry = result[i]

    # Convert to a list
    return [v for v in result.values()]


def single_parse(string):
    """
    Converts the string into a list of all the digits. This is a unique case where there are only
    7 digits
    :param string: the input string 
    :return: a list of all the characters
    """
    return list(string)


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
@click.argument('numbers', nargs=-1, required=1)
def main(numbers):
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

    # nargs = -1 is used in click to allow multiple arguments and it turns it into a list
    for digits in numbers:
        if digits:
            length = len(digits)
            if FEWEST_DIGITS <= length <= MOST_DIGITS:
                parse(digits)


if __name__ == '__main__':
    main()
