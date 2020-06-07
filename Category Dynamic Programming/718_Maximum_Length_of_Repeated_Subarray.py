from typing import List, Tuple

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

    def findLength(self, A: List[int], B: List[int]) -> Tuple:
        memo = {}
        
        def DP(i: int, j: int) -> int:
            if i<0 or j<0:
                return 0, 0

            if (i, j) in memo:
                return memo[(i, j)]
                
            maxim = 0
            matchedLength = 0
            res = DP(i-1, j-1)
            if A[i] == B[j]:
                matchedLength = res[1] + 1
                maxim = matchedLength

            maxim = max(maxim, res[0])
            maxim = max(maxim, DP(i-1, j)[0])
            maxim = max(maxim, DP(i, j-1)[0])

            memo[(i, j)] = maxim, matchedLength
            return memo[(i, j)]
        
        return DP(len(A)-1, len(B)-1)[0]


if __name__ == "__main__":
    s = Solution()
    print(s.findLength([0,0,0,0,0], [0,0,0,0,0]))
    print(s.findLength([5,14,53,80,48], [50,47,3,80,83]))
    print(s.findLength([1,2,3,2,1], [3,2,1,4,7]))