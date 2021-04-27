from os import truncate


class Solution:
    def _cal(self, numbers, operators) -> int:
        if not numbers:
            return 0

        if not operators:
            if numbers:
                n = 0
                i = 0
                while numbers:
                    n += numbers.pop() * 10 ** i
                    i += 1
                return n
            else:
                return 0

        test = False

        if len(operators) > len(numbers):
            test = True
        else:
            test = False

        o = operators.pop()

        n1 = 0
        i = 0
        n2 = 0

        if numbers:
            n2 = numbers.pop()

            if test:
                n1 = 0
            else:
                while numbers:
                    n1 += numbers.pop() * 10 ** i

                    if operators:
                        break

                    i += 1

        if o == "+":
            n = int(n2) + int(n1)
        elif o == "-":
            n = int(n1) - int(n2)
        else:
            n = n2
            numbers.append(n)

            n = self._cal(numbers, operators)

        return n

    def calculate(self, s: str) -> int:
        if not s:
            return 0
        numbers = []
        operators = []

        for s1 in s:
            if s1.isdigit():
                numbers.append(int(s1))
            elif s1 != " ":
                if operators:
                    if s1 == "(":
                        operators.append(s1)
                        continue

                    if (s1 == "+" or s1 == "-") and operators[-1] == "(":
                        operators.append(s1)
                        continue

                    if s1 == ")":
                        n = self._cal(numbers, operators)

                        numbers.append(n)

                        if operators:
                            operators.pop()
                        continue

                    n = self._cal(numbers, operators)

                    numbers.append(n)
                    operators.append(s1)
                    print(numbers, end=",")
                    print(operators)
                    print("\n")
                else:
                    operators.append(s1)

        n = self._cal(numbers, operators)

        numbers.append(n)

        return numbers.pop()


test = "12-(+3-1)"
obj = Solution()

print(obj.calculate(test))