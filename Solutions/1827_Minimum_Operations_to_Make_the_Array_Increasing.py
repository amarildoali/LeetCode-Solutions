from typing import List


def minOperations(self, nums: List[int]) -> int:
    result = 0
    for i in range(len(nums) - 1):
        if nums[i] >= nums[i + 1]:
            diff = nums[i] - nums[i + 1]
            nums[i + 1] += diff + 1
            result += diff + 1
    return result
