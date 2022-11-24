from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for i in range(len(accounts)):
            wealth_i = 0
            for j in range(len(accounts[i])):
                wealth_i += accounts[i][j]
            if wealth_i > max:
                max = wealth_i
        return max
