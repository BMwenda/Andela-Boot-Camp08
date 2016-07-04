def fizz_buzz(n):
    """Return fizz when divisible by 3 \
    return buzz when divisible by 5 \
    return fizzbuzz when divisible by both 3 and 5"""

    # Check for null values
    if n == '':
        raise Exception("No argument passed")

    # Confirm that n is an integer
    if type(n) is not int:
        raise TypeError("Only integers are allowed")

    # Raise error if number is negative
    if n < 0:
        raise Exception("Only positive integers allowed")

    # Check for zero, since 0 % n is always 0.
    if n == 0:
        return 0

    if n % 15 == 0:
        return 'fizzbuzz'
    elif n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'
    else:
        return n
