from typing import List


def minOperations(nums: List[int]) -> int:
    result = 0
    for i in range(len(nums) - 1):
        if nums[i] >= nums[i + 1]:
            diff = nums[i] - nums[i + 1]
            nums[i + 1] += diff + 1
            result += diff + 1
    return result


A = [1, 5, 2, 4, 1]
print(len(A))
print(minOperations(A))
