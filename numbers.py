import math


def is_prime(num):
    """check whether num is prime"""
    if num < 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        sqrt_num = int(math.sqrt(num))