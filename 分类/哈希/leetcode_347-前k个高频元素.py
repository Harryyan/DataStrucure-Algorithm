from typing import List, DefaultDict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = DefaultDict(int)
        result = []

        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        x = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)}

        i = 0

        for key in x:
            if i < k:
                i += 1
                result.append(key)

        return result

        

class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = DefaultDict(int)
        bucket = {k:[] for k in range(1, len(nums)+1)}
        result = []

        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1


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

s = Solution()
nums = [5,1,-1,-8,-7,8,-5,0,1,10,8,0,-4,3,-1,-1,4,-5,4,-3,0,2,2,2,4,-2,-4,8,-7,-7,2,-8,0,-8,10,8,-8,-2,-9,4,-7,6,6,-1,4,2,8,-3,5,-9,-3,6,-8,-5,5,10,2,-5,-1,-5,1,-3,7,0,8,-2,-3,-1,-5,4,7,-9,0,2,10,4,4,-4,-1,-1,6,-8,-9,-1,9,-9,3,5,1,6,-1,-2,4,2,4,-6,4,4,5,-5]
r = s.topKFrequent(nums, 7)

print(r)