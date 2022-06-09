def add(x, y):
    """Add two numbers Function"""
    return x+y

def sub(x, y):
    """Substract from two number Function"""
    return x-y

def multi(x, y):
    """Multiply from two number Function"""
    return x*y


def divided(x, y):
    """Divied from two number Function"""
    if y == 0:
        raise ValueError("Can't divide by 0")
    return x/y

