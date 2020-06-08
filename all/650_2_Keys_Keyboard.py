from math import inf

class Solution:
    def minSteps(self, n: int) -> int:
        memo = {}
        memo[(1, None)] = 0
        
        def DP(n: int, k: int) -> int:
            if (n, k) in memo:
                return memo[(n, k)]

            if k != None:
                if n == k:
                    memo[n, k] = DP(n, None) + 1
                else:
                    memo[n, k] = DP(k, k) + ((n // k) - 1)                
            else:
                minim = inf
                for i in range (n-1, (n-1)//2, -1):
                    j = n - i
                    if i%j == 0:
                        minim = min(minim, DP(i, j) + 1 )
        
                memo[n, k] = minim
            return memo[n, k]
        
        return DP(n, None)

if __name__ == "__main__":
    s = Solution()
    print(s.minSteps(9))