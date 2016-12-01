def perfSquare(a):
    if a > 0:
        b = a**(1/2)            # Calculate square root of a
        c = b - b % 1             # Round the square root down
    else:
        return "Number must be a positive integer."
    return int(c**2)            # Calculate the highest perfect square
