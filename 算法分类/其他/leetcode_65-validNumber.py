# A valid number can be split up into these components (in order):

# A decimal number or an integer.
# (Optional) An 'e' or 'E', followed by an integer.
# A decimal number can be split up into these components (in order):

# (Optional) A sign character (either '+' or '-').
# One of the following formats:
# One or more digits, followed by a dot '.'.
# One or more digits, followed by a dot '.', followed by one or more digits.
# A dot '.', followed by one or more digits.
# An integer can be split up into these components (in order):

# (Optional) A sign character (either '+' or '-').
# One or more digits.
# For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

# Given a string s, return true if s is a valid number.

class Solution:
    def isNumber(self, s: str) -> bool:
        # DFA transitions: dict[action] -> successor
        states = [{},
                  # state 1
                  {"sign":2,"digit":3,"dot":4},
                  # state 2
                  {"digit":3,"dot":4},
                  # state 3
                  {"digit":3,"dot":5,"e|E":6},
                  # state 4
                  {"digit":5},
                  # state 5
                  {"digit":5,"e|E":6},
                  # state 6
                  {"sign":7,"digit":8},
                  # state 7
                  {"digit":8},
                  # state 8
                  {"digit":8}]

        def strToAction(st):
            if '0' <= st <= '9':
                return "digit"
            if st in "+-":
                return "sign"
            if st in "eE":
                return "e|E"
            if st == '.':
                return "dot"
            return None

        currState = 1
        for c in s:
            action = strToAction(c)
            if action not in states[currState]:
                return False
            currState = states[currState][action]

        # ending states: 3,5,8,9
        return currState in {3,5,8,9}

str = "0"
s = Solution()

print(s.isNumber(str))