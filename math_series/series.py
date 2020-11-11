def fibonacci(n):
    if n < 0:
        return None
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))


def lucas(n):
    """ 
    adds previous value to next value. starts with 2 and 1. 
    returns nth value
    """ 
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

def sum_series(n, a=0, b=1):
    """ 
    takes in one required perameter and two optional parameters
    req perameter determines which series will be printed
    perammeters call previous functions.
    no optional arg print fibonacci
    arguments 2 and 1 print lucas
    """
    if n
