
# 题目:
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。


def isValid(str):
    hash_table = {"{": "}", "[": "]", "(": ")"}
    stack = []

    for item in str:
        if item in hash_table.keys():
            stack.append(item)
        elif stack:
            left = stack.pop()

            if item != hash_table[left]:
                return False
            else:
                continue
        else:
            return False

    return not stack


result = isValid("{]")
print(result)
