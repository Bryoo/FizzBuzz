
def fizz_buzz(n):

    if n % 3 == 0 and n % 5 == 0:
        # Divisible by both 3 and 5
        return 'FizzBuzz'

    elif n % 3 == 0:
        # Divisible by 3
        return 'Fizz'

    elif n % 5 == 0:
        # Divisible by 5
        return 'Buzz'

    else:
        # Not divisible by wither 5 or 5
        return n

