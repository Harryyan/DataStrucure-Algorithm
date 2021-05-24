from typing import Counter


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        queue_1 = []
        queue_2 = []

        for s1 in s:
            if s1 == "#":
                if queue_1:
                    queue_1.pop()
            else:
                queue_1.append(s1)

        for t1 in t:
            if t1 == "#":
                if queue_2:
                    queue_2.pop()
            else:
                queue_2.append(t1)

        if len(queue_1) != len(queue_2):
            return False
        else:
            return queue_1 == queue_2


test = Solution()
s = "abc#"
t = "abc#"
print(test.backspaceCompare(s, t))
