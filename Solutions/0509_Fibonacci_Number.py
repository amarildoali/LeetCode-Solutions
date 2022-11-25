class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        fibo = [0, 1]
        for i in range(n - 1):
            fibo.append(fibo[i] + fibo[i+1])
        return fibo[-1]
