from typing import List


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        new_set = set(nums)
        for i in nums:
            new_set.add(int(str(i)[::-1]))
        return len(new_set)
