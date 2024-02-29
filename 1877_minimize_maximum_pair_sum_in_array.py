from typing import List


def minPairSum(nums: List[int]) -> int:
    A = []
    nums.sort()
    for i in range(0, int(len(nums)/2)):
        A.append(nums[i] + nums[-i-1])
    return max(A)
