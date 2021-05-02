import math


def sqrt(x):
    """
    求平方根，精确到小数点后6位
    """
    low = 0
    mid = x / 2
    high = x
    while abs(mid ** 2 - x) > 0.0000001:
        if mid ** 2 < x:
            low = mid
        else:
            high = mid
        mid = (low + high) / 2
    return round(mid, 6)


def sqrt_0(x):
    if x <= 1:
        return x

    left = 1
    right = x >> 1
    while left < right:
        mid = (left + right + 1) >> 1
        if mid * mid > x:
            right = mid - 1
        else:
            left = mid
    return left


print(sqrt_0(16))
