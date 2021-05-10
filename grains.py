def square(number: int) -> int:
    """Return the value of grain at a particular square on the chess board."""
    if 65 > number > 0:
        double = 1
        for num in range(1, number):
            double *= 2
        return double
    else:
        raise ValueError("Number must be between 1 and 64.")


def total() -> int:
    """Return the total number of grains on the chess board."""
    double = 1
    for num in range(1, 65):
        double *= 2
    return double-1
