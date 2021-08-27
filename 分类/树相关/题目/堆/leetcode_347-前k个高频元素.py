from typing import List, Counter
import collections
import heapq


# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = Counter(nums) # most common 可以返回前K个
        result = []

        x = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)}

        i = 0

        for key in x:
            if i < k:
                i += 1
                result.append(key)

        return result

        

class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = Counter(nums)
        bucket = {k:[] for k in range(1, len(nums)+1)}
        result = []

        for key in dict:
            freq = dict.get(key)
            bucket[freq].append(key)

        x = k

        for key in reversed(bucket):
            if len(bucket[key]) > 0:
                if len(bucket[key]) == x:
                    result += bucket[key]
                    break

                if len(bucket[key]) < x:
                    x = k - len(bucket[key])
                    result += bucket[key]

            else: continue

        return result[0:k]

# 堆排序，使用小顶堆; 堆内元素不超过K个；如果到了K个，频率大于堆顶元素的，才能更新堆
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        heap = [(val, key) for key, val in count.items()]
        return [item[1] for item in heapq.nlargest(k, heap)]

s = Solution()
nums = [5,1,-1,-8,-7,8,-5,0,1,10,8,0,-4,3,-1,-1,4,-5,4,-3,0,2,2,2,4,-2,-4,8,-7,-7,2,-8,0,-8,10,8,-8,-2,-9,4,-7,6,6,-1,4,2,8,-3,5,-9,-3,6,-8,-5,5,10,2,-5,-1,-5,1,-3,7,0,8,-2,-3,-1,-5,4,7,-9,0,2,10,4,4,-4,-1,-1,6,-8,-9,-1,9,-9,3,5,1,6,-1,-2,4,2,4,-6,4,4,5,-5]
r = s.topKFrequent(nums, 7)

print(r)