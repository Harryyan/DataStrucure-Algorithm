
# 给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。

# 注意：如果对空文本输入退格字符，文本继续为空。


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        
        for item in s:
            if item != '#':
                stack1.append(item)
            else:
                if stack1:
                    stack1.pop()
        
        for item in t:
            if item != '#':
                stack2.append(item)
            else:
                if stack2:
                    stack2.pop()
            print(item)
                
        return stack1 == stack2
    
s = Solution()
S = "y#fo##f"
T = "y#f#o##f"

r = s.backspaceCompare(S, T)

print(r)