from typing import List

# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have 
# to wait after the ith day to get a warmer temperature. If there is no future 
# day for which this is possible, keep answer[i] == 0 instead.

class Solution:
    # tc: O(n ^ 2)
    # sc: O(n)
    def dailyTemperatures(self, temperatures):
        stack, ret = [], [0] * len(temperatures)

        for i, num in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < num:
                index = stack.pop()
                ret[index] = i - index
            stack.append(i)
        return ret


temperatures = [73,74,75,71,69,72,76,73]
s = Solution()