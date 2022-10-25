def main(a):
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    b = a**(1/2)
    if a==(int(b))**2:
        m = True
    else:
        m = False
    # Write your code here
    return m 