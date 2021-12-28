# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ret = 0
        lg = len(s)
        for i in range(lg):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ret = max(ret, i - stack[-1])
                    print(ret)
        return ret