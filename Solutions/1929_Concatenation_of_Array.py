from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = [x for x in nums]
        for i in nums:
            result.append(i)
        return result
