from math import inf


class Solution:
    def __init__(self):
        self.mem = {}
        

    def DP(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n in self.mem:
            return self.mem[n]

        maxim = -inf
        for i in range(1, (n//2) + 1):
            maxim = max(maxim, max(i, self.DP(i)) * max((n-i), self.DP(n-i)))

        self.mem[n] = maxim
        return maxim

    def integerBreak(self, n: int) -> int:
        res = self.DP(n)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.integerBreak(2))
    print(s.integerBreak(10))