from typing import List

class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        memo = {}
        aSet = set(A)

        def DP(d, s):
            if s not in aSet:
                return 1
            elif s <= d // 2:
                return 2

            if (d, s) in memo:
                return memo[(d, s)]

            res = 1 + DP(s, d-s)
            memo[(d, s)] = res
            return res


        maxim = 0
        for i in range (1, len(A)):
            for j in range (0, i):
                maxim = max(maxim, DP(A[i], A[j]))

        return 0 if maxim <= 2 else maxim


if __name__ == "__main__":
    s = Solution()
    print(s.lenLongestFibSubseq([1,2,3,4,5,6,7,8]))
    print(s.lenLongestFibSubseq([1,3,7,11,12,14,18]))
    print(s.lenLongestFibSubseq([1,3,4,7,10,11,12,18,23,35]))