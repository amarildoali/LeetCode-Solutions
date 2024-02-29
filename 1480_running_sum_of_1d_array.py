from functools import reduce
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.append(reduce(lambda a, b: a + b, nums[:i + 1]))
        return result
