# You are playing a Flip Game with your friend.
# You are given a string currentState that contains only '+' and '-'. You and your friend take turns to flip two consecutive "++" into "--". 
# The game ends when a person can no longer make a move, and therefore the other person will be the winner.
# Return true if the starting player can guarantee a win, and false otherwise.

class Solution(object):

    # tc: O(n^2)
    # sc: O(n)

    # 遍历所有可能性

    def __init__(self):
        self.memo = {}

    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s in self.memo:
            return self.memo[s]
        
        for i in range(len(s) - 1):
            if s[i] == "+" and s[i+1] == "+":
                temp = s[:i] + "--" + s[i+2:]
                # 看对手赢不赢的了，对手赢不了，说明当前我们这样翻(temp)是True的
                if not self.canWin(temp):
                    self.memo[s] = True
                    return True
        
        # 假如说发现对手都赢的了，那么当前s我们怎么翻都是输
        # 把当前s记录成False
        self.memo[s] = False
        
        return self.memo[s]

s = "++--++++--+++"
so = Solution()

print(s)
r = so.canWin(s)

print(r)