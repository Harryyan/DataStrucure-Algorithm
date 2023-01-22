
import heapq
import bisect
from typing import Counter
from itertools import permutations, combinations, combinations_with_replacement


mylist = list(range(1,1000))
mytuple = tuple(range(-5,5,2))

# 优先级队列
print(mytuple)
print(heapq.nsmallest(4,mytuple) )


# 字典相关 - 记录元素出现个数
nums = [1,1,1,1,1,2,3,1,2,4,2,2,1,2,3]
num_dict = Counter(nums)

print(num_dict)

a = [1,4,6,8,12,15,20]
position = bisect.bisect(a,13)
print(position)


# Bisect - 针对有序数组，进行二分查找

breakpoints = [25,50,75]
classes = ['Below 25', '25 to 50', '50 to 75', '75 and above']
scores  = [1,3,23,6,34,3456,5,62,4234]
[classes[ bisect(breakpoints, score) ] for score in scores]



# permutation & combination
list( permutations('ABCD',2) )   # 有重复 例如AB,BA
list( combinations('ABCDE',2) )  # 没重复，不包含自己
list( combinations_with_replacement('ABCDE',2) )  # 没重复，包含自己， 例如AA,BB