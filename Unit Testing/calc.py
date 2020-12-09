# calc.py


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError("Can't divide by zero!")
    return x / y


def integer_division(x, y):
    """Interger division function"""
    if y == 0:
        raise ValueError("Can't integer divide by zero!")
    return x // y


def modulus(x, y):
    """Modulus function"""
    if y == 0:
        raise ValueError("Can't modulus by zero!")
    return x % y


def exponentiation(x, y):
    """Exponentiation function"""
    return x ** y