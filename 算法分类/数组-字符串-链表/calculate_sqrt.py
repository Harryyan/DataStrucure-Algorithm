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


print(sqrt_0(3))


def deletion_distance(str1, str2):
    if str1 == str2: 
     return 0
  
    m = len(str1)
    n = len(str2)
  
    if n == 0 and m != 0:
        return m

    if m == 0 and n != 0:
        return n
  
    # Sentinel
    dp =[[0 for i in range(n + 1)] for _ in range(m + 1)] 
    
    # tc: O(mn)
    # sc: O(mn)
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
    
    print(dp)
    return dp[-1][-1]

r = deletion_distance('abc','aef')
print(r)