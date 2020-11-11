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
    

def sum_series():
    """ 
    takes in one required perameter and two optional parameters
    req perameter determines which series will be printed
    perammeters call previous functions.
    no optional arg print fibonacci
    arguments 2 and 1 print lucas

    """
    pass