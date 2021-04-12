def sqrt(x):
    '''
    求平方根，精确到小数点后6位
    '''
    low = 0
    mid = x / 2
    high = x
    while abs(mid ** 2 - x) > 0.000000000001:
        if mid ** 2 < x:
            low = mid
        else:
            high = mid
        mid = (low + high) / 2
    return round(mid, 6)


print(sqrt(101))
