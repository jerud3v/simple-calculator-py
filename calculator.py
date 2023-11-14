import re

valid_operators = ['+', '-', '*', '/']


def validate_number(number):
    """This will check if the input number is valid for mathematical operations."""
    regex_pattern = r"^(?P<sign>[-+])?(?P<integer>\d+)(?:\.(?P<decimals>\d+))?(?P<exponent>e[+-]?\d+)?$"
    is_matched = re.search(regex_pattern, number)
    if is_matched:
        return number
    else:
        raise ValueError(f'The {number} is invalid.')


def get_user_input():
    """Gets users input for the operation and numbers to calculate """
    combined_operations = ' '.join(valid_operators)
    operator = input(f"Enter the operation ({combined_operations}): ")
    if operator not in valid_operators:
        raise ValueError(f'The selected ({operator}) operator is invalid')

    number_first = input("Enter the first number: ")
    number_first = validate_number(number_first)
    number_second = input("Enter the second number: ")
    number_second = validate_number(number_second)

    return operator, float(number_first), float(number_second)


def calculate(operation, number_first, number_second):
    """Calculates the result of the given operation on the given numbers."""
    try:
        if operation == "+":
            return number_first + number_second
        elif operation == "-":
            return number_first - number_second
        elif operation == "*":
            return number_first * number_second
        elif operation == "/":
            if number_first == 0 or number_second == 0:
                return 0
            return number_first / number_second
    except (ValueError, ZeroDivisionError) as e:
        print(f'Something went wrong: {e}')


def display_result(result):
    """Displays the result of the calculation to the user."""
    print(f"The result is: {result:g}")


def main():
    global valid_operators
    to_exit = False
    while not to_exit:
        try:
            operation, number_first, number_second = get_user_input()
            result = calculate(operation, number_first, number_second)
            display_result(result)

            again = input('Do you want to calculate again? (y/N): ')
            if again.lower() != 'y':
                to_exit = True
        except ValueError as e:
            print(e)


main()
print('Goodbye!')
