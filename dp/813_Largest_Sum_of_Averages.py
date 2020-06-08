from typing import List
from math import inf

class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        memo = {}

        cumSum = [0]
        for i in range(len(A)):
            cumSum.append(cumSum[i] + A[i])

        def average(i, j):
            count = j-i+1
            summ = cumSum[j+1] - cumSum[i]
            return summ / count

        def DP(index: int, level: int):
            if index < 0:
                return 0
            
            if (index, level) in memo:
                return memo[(index, level)]

            maxim = 0
            if level == 1:
                maxim = average(0, index)
            else:
                for i in range (index+1):
                    maxim = max(maxim, DP(i-1, level-1) + average(i, index))
            
            memo[(index, level)] = maxim
            return maxim

        return DP(len(A)-1, K)


if __name__ == "__main__":
    s = Solution()
    print(s.largestSumOfAverages([2561,9087,398,8137,7838,7669,8731,2460,1166,619], K = 3))