def fibonacci(n):

    """Return the nth value in the fibonacci series.
    Parameters:
    n: The index of the fibonacci value to return.
    Returns:
    The fibonacci value at the given index.
    """
     
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """Return the nth value in the lucas series.
    Parameters:
    n : The index of the lucas value to return.
    Returns:
    The lucas value at the given index.
    """ 
    if n < 0:
        return None
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, first=0, second=1):

    """Return the nth value in a custom series.
    Parameters:
    n: The index of the series value to return.
    first: The first value of the series. Default is 0 for fibonacci series.
    second: The second value of the series. Default is 1 for fibonacci series.
    Returns:
    The series value at the given index.
    """
    if n < 0:
        return None
    elif n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n-1, first, second) + sum_series(n-2, first, second)