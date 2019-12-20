from typing import List

class Solution:
    # def findLength(self, A: List[int], B: List[int]) -> int:
    #     table = [[0] * len(B) for _ in range(len(A))]

    #     maxim = 0
    #     for i in range(len(A)):
    #         if A[i] == B[0]:
    #             table[i][0] = 1
    #             maxim = 1

    #     for j in range(len(B)):
    #         if A[0] == B[j]:
    #             table[0][j] = 1
    #             maxim = 1

    #     for i in range(1, len(A)):
    #         for j in range(1, len(B)):
    #             if A[i] == B[j]:
    #                 table[i][j] = 1 + table[i-1][j-1]
    #                 maxim = max(maxim, table[i][j])

    #     return maxim

    def findLength(self, A: List[int], B: List[int]) -> int:
        memo = {}

        def DP(i: int, j: int, matchCount: int) -> int:
            if i<0 or j<0:
                return matchCount
                
            if (i, j, matchCount) in memo:
                return memo[(i, j, matchCount)]

            maxim = 0
            if A[i] == B[j]:
                maxim = DP(i-1, j-1, matchCount+1)

            maxim = max(maxim, max(DP(i-1, j, 0), DP(i, j-1, 0)))

            memo[(i, j, matchCount)] = maxim
            return maxim

        
        return DP(len(A)-1, len(B)-1, 0)


if __name__ == "__main__":
    s = Solution()
    print(s.findLength([1,2,3,2,1], [3,2,1,4,7]))