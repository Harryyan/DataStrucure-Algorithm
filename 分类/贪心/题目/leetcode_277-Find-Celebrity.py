
# Suppose you are at a party with n people (labeled from 0 to n - 1), and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her, but he/she does not know any of them.

# Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

# You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

# The knows API is already defined for you.
# return a bool, whether a knows b

def knows(a: int, b: int) -> bool:
    return True

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 我们先初始化候选人为第一个人        
        candidate = 0

        # 观察图可知，每个节点，最多只有一个箭头
        # 另一个规律是，假如说有一个名人，那么所有的箭头都指向他
        # 所以，假如说真有一个名人，那么我们任意找到一个箭头的指向，都会指向那个名人
        for j in range(1, n):
            # 假如 candidate认识j
            if knows(candidate, j): 
                candidate = j

        
        # 判断是否符合条件
        for j in range(n):
            # 名人只认识自己，跳过
            if candidate == j:
                continue
            # 假如发现名人还认识别人，说明它不是名人
            if knows(candidate, j):
                return -1
            # 假如别人不认识名人，说明它不是名人
            if not knows(j, candidate):
                return -1
        
        return candidate
