class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(300):
            if i % n == 0 and i % 2 == 0:
                if i != 0:
                    return i
