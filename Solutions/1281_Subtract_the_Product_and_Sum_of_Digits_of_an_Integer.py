from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        S = [int(x) for x in str(n)]
        return reduce(lambda a, b: a * b, S) - reduce(lambda a, b: a + b, S)
