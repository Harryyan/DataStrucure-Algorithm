from typing import List


class Solution:
    result = 0
    max_value = 0

    def backPack(self, list: List, max: int, values: list):
        def f(
            index: int, cv: int, n: int, max: int, items: list, value: int, values: list
        ):
            if index > n - 1:
                if cv > self.result and value > self.max_value:
                    self.result = cv
                    self.max_value = value
                return
            f(index + 1, cv, n, max, items, value, values)
            if cv + items[index] <= max:
                f(
                    index + 1,
                    cv + items[index],
                    n,
                    max,
                    items,
                    value + values[index],
                    values,
                )

        f(0, self.result, len(list), max, list, 0, values)
        return self.result, self.max_value


a = Solution()
values = [3, 2, 1]
b, c = a.backPack([1, 3, 6], 5, values)
print(b)
print(c)