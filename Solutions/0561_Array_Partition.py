from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        S = sorted(nums)
        result = 0
        for i in range(0, len(S), 2):
            result += min(S[i], S[i+1])
        return result
