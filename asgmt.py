def use_abs_function(x: int) -> int:
    """
    >>> use_abs_function(-2)
    2
    >>> use_abs_function(-3)
    3
    >>> use_abs_function(0)
    0
    >>> use_abs_function(2)
    2
    >>> use_abs_function(3)
    3
    """
    ### BEGIN SOLUTION
    if x>=0:
      return x
    else return -x
    ### END SOLUTION
