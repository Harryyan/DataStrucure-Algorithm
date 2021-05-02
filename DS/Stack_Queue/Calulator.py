class Solution(object):
    def calculate(self, s):
        res, num, sign = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == "+" or c == "-":
                res += sign * num
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res += sign * num
        return res

    def _cal(self, operators, numbers):
        o = operators.pop()
        n = numbers.pop()
        n0 = 0

        if o == "+":
            if numbers:
                n0 = numbers.pop()
            result = n0 + n
            numbers.append(result)

        if o == "-":
            if numbers:
                n0 = numbers.pop()
            result = n0 - n
            numbers.append(result)

        if o == "*":
            if numbers:
                n0 = numbers.pop()
            result = n0 * n
            numbers.append(result)

        if o == "/":
            if numbers:
                n0 = numbers.pop()
            result = n0 // n
            numbers.append(result)

    def recursive_cal(self, s, operators, numbers):
        if not operators or self.shouldAppend(s, operators[-1]):
            operators.append(s)
        else:
            self._cal(operators, numbers)
            self.recursive_cal(s, operators, numbers)

    def calculator_basic(self, str: str):
        numbers = []
        operators = []
        num = 0

        for s in str:
            if s.isdigit():
                num = 10 * num + int(s)
            elif s != " ":
                numbers.append(num)
                num = 0

                if not operators:
                    operators.append(s)
                else:
                    self.recursive_cal(s, operators, numbers)

        numbers.append(num)
        num = 0

        while operators:
            self._cal(operators, numbers)

        return numbers.pop()

    def shouldAppend(self, current, pre):
        if current == "*" and (pre in "+-"):
            return True

        if current == "/" and (pre in "+-"):
            return True

        return False


class Solution2:
    def calculate(self, s):
        stack = []
        pre_op = "+"
        num = 0
        for i, each in enumerate(s):
            print(each)
            if each.isdigit():
                num = 10 * num + int(each)

            if i == len(s) - 1 or each in "+-*/":
                if pre_op == "+":
                    stack.append(num)
                elif pre_op == "-":
                    stack.append(-num)
                elif pre_op == "*":
                    stack.append(stack.pop() * num)
                elif pre_op == "/":
                    top = stack.pop()
                    if top < 0:
                        stack.append(int(top / num))
                    else:
                        stack.append(top // num)

                pre_op = each
                num = 0
        return sum(stack)


test = Solution()
test2 = Solution2()
str = "123-(-13+2) + 13 - 2 + (9 + 4)"
# print(test.calculate(str))

print("######################")
str_basic = "3+2*2"
print(test2.calculate(str_basic))