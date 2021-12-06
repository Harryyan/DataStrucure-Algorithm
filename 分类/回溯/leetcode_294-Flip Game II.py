# You are playing a Flip Game with your friend.
# You are given a string currentState that contains only '+' and '-'. You and your friend take turns to flip two consecutive "++" into "--". 
# The game ends when a person can no longer make a move, and therefore the other person will be the winner.
# Return true if the starting player can guarantee a win, and false otherwise.

from functools import lru_cache

class Solution:
    @lru_cache(None)
    def canWin(self, s: str) -> bool:
        length = len(s)
        for i in range(length - 1):
            if s[i] == "+" and s[i + 1] == "+":
                if not self.canWin(s[:i] + "--" + s[i + 2:]):
                    return True
        return False
