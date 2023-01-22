
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
                
        return stack1 == stack2


# 准备两个指针 ii, jj 分别指向 SS，TT 的末位字符，再准备两个变量 skipSskipS，skipTskipT 来分别存放 SS，TT 字符串中的 # 数量。
# 从后往前遍历 SS，所遇情况有三，如下所示：
# 2.1 若当前字符是 #，则 skipSskipS 自增 11；
# 2.2 若当前字符不是 #，且 skipSskipS 不为 00，则 skipSskipS 自减 11；
# 2.3 若当前字符不是 #，且 skipSskipS 为 00，则代表当前字符不会被消除，我们可以用来和 TT 中的当前字符作比较。
# 若对比过程出现 SS, TT 当前字符不匹配，则遍历结束，返回 falsefalse，若 SS，TT 都遍历结束，且都能一一匹配，则返回 truetrue。


class Solution2:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        skipS = skipT = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == "#":
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if T[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        
        return True

    
s = Solution()
S = "y#fo##f"
T = "y#f#o##f"

r = s.backspaceCompare(S, T)

print(r)