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

    # Is in the range of 1 to 59
    return LOWEST_NUMBER <= number <= HIGHEST_NUMBER


def get_value(position, valid_digits, entries, previous_entry):
    """
    A valid number to take is if it is a number between 1 and 59 going left to right
    :param position: the current position
    :param valid_digits: 
    :param entries: 
    :param previous_entry: 
    :return: 
    """
    value = None

    # Just a nice variable for better understanding in this example
    current_entry = entries[position]

    if valid_digits[position]:
        # If the first digit is a valid digit, we grab it
        value = entries[position]
    elif not valid_digits[position] and valid_digits[position + 1]:
        # If the first double digit is not valid and the next double digit by traversing one digit is valid, we grab
        value = current_entry[0]

    # if value == current_entry:
    #     return value[0]
    if not value or value == previous_entry:
        # If no value is grabbed or if we have a double, then we don't return a value
        return None
    else:
        return value


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


def has_duplicates(digits):
    return len(digits) != len(set(digits))


def parse(digits):
    """
    If we are over 7 digits and under 15 digits, we will have atleast 1 digit that requires that there be a 
    double digits
    :param digits: 
    :return: 
    """
    num_of_doubles = (len(digits) - UNIQUE_NUMBER)

    # If there are only 7 digits, then we just return a list of all the digits
    if num_of_doubles == 0:
        return list(digits)

    # Get all the potential double digits
    doubles = [digits[i:i + 2] for i in range(0, len(digits))]

    # Validate if they are between 1 and 59
    valid_digits = [is_valid(i) for i in doubles]

    result = []
    previous_entry = None

    # Used as a skipper so because I use the enumerator and maybe there is a better way cause i would like
    # to do i+1 where skip = True
    skip = False

    for i, first_entry in enumerate(doubles):
        # Skip if this is set, this is like making i+1 so that it would enumerate after the next digit
        if skip:
            skip = False
            continue

        # Get the valid number
        value = get_value(i, valid_digits, doubles, previous_entry)

        # Only add the value if it is not in the result list
        if value:
            # If it is not a duplicate, add it. If not, just add the left digit
            if value not in result:

                # Add it to the list and store the value as a previous entry for the next for loop iteration
                result.append(value)
                previous_entry = value

                # Check to see if the result is a double-digit
                is_double_digit = len(value) == 2

                # If the value is bigger than 10, it is a double digit and we only have a certain amount of
                # double digits, so once we get to zero, we just split the rest of the string into the result
                if is_double_digit:
                    num_of_doubles -= 1

                # Check to see if a value is in a list
                if num_of_doubles == 0:

                    # Split the rest of the list and put it into the result
                    end = list(digits[i + 2:])

                    # Only add it if the values don't have any duplicates in it
                    if not has_duplicates(end):
                        result += end
                    break

                elif is_double_digit:
                    # Since it's a double-digit, we want to skip two numbers for iterating through the loop
                    skip = True
            else:
                # Check to see if we can add just the left digit
                value = value[0]
                if value not in result:
                    # Add this value
                    result.append(value)

    return result


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

    [ "569815571556", “4938532894754”, “12345617”, “472844278465445”]

    Your function should return:

    4938532894754 -> 49 38 53 28 9 47 54
    1234567 -> 1 2 3 4 5 6 7
    """

    # nargs = -1 is used in click to allow multiple arguments and it turns it into a list
    for digits in numbers:
        if digits:
            length = len(digits)

            # Check to make sure we are between 7 and 14 digits. If not, we don't continue
            if FEWEST_DIGITS <= length <= MOST_DIGITS:
                lucky_numbers = parse(digits)

                # Calls the display function
                display(digits, lucky_numbers)


if __name__ == '__main__':
    main()
