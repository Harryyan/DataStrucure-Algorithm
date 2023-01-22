from typing import List
import bisect

# Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.

# Implement the SummaryRanges class:

# SummaryRanges() Initializes the object with an empty stream.
# void addNum(int val) Adds the integer val to the stream.
# int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi].


# leetcode - 352

class SummaryRanges:

    # tc: O(nlogn)
    # sc: O(n)
    def __init__(self):
        self.res = []

    def addNum(self, val: int) -> None:
        if val not in self.res:
            self.res.append(val)
            

    def getIntervals(self) -> List[List[int]]:
        self.res.sort() #排序
        # 读出
        out= []
        left = self.res[0]
        for i in range(1,len(self.res)):
            if self.res[i] == self.res[i-1] + 1:
                continue
            else:
                out.append([left,self.res[i-1]])
                left = self.res[i]
        out.append([left,self.res[-1]])

        return out