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
                    if self.shouldAppend(s, operators[-1]):
                        operators.append(s)
                    else:
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
                            result = n0 / n
                            numbers.append(result)
                        operators.append(s)

        numbers.append(num)
        num = 0

        []
        while operators:
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
                result = n0 / n
                numbers.append(result)

        return numbers.pop()

    def shouldAppend(self, current, pre):
        if current == "*" and (pre == "+" or pre == "-"):
            return True

        if current == "/" and (pre == "+" or pre == "-"):
            return True

        return False


test = Solution()
str = "123-(-13+2) + 13 - 2 + (9 + 4)"
print(test.calculate(str))

print("######################")
str_basic = "3 + 4 - 99"
print(test.calculator_basic(str_basic))