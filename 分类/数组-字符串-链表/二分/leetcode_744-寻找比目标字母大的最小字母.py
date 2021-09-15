from typing import List

# 给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。
# 在比较时，字母是依序循环出现的。举个例子：

# 如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters) - 1

        while low <= high:
            mid = low + ((high - low) >> 1)

            if letters[mid] <= target:
                low = mid + 1
            else:
                if mid - 1 >= 0 and letters[mid - 1] <= target:
                    return letters[mid]
                else:
                    high = mid - 1

        return letters[0]

        
letters = ["c", "f", "j"]
target = "k"
s = Solution()

r = s.nextGreatestLetter(letters, target)

print(r)