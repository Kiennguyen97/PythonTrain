
from functools import wraps, partial, update_wrapper, partialmethod




def bai2():
    """
    bai2
    """
    pass


def power(a, b):
    return a ** b




if __name__ == '__main__':
    # bai2()


    pow2 = partial(power, b=2)
    pow4 = partial(power, b=4)
    power_of_5 = partial(power, 5, 3)

    print(power(2, 3))
    print(pow2(4))
    print(pow4(3))
    print(power_of_5())