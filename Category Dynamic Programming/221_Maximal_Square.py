from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])

        DP = [[0 for _ in range(n)] for _ in range(m)]
        maxSquare = 0
        for i in range(m):
            DP[i][0] = int(matrix[i][0])
            if DP[i][0] == 1:
                maxSquare = 1
            
        for j in range(1, n):
            DP[0][j] = int(matrix[0][j])
            if DP[0][j] == 1:
                maxSquare = 1

        for i in range(1, m):
            for j in range(1, n):
                if int(matrix[i][j]) == 1:
                    localMax= min(DP[i-1][j-1], min(DP[i-1][j], DP[i][j-1])) + 1
                    
                    if localMax > maxSquare:
                        maxSquare = localMax

                    DP[i][j] = localMax
        
        return maxSquare * maxSquare


if __name__ == "__main__":
    s = Solution()
    print(s.maximalSquare([['1','0','1','0','0'],
                           ['1','0','1','1','1'],
                           ['1','1','1','1','1'],
                           ['1','0','0','1','0']]))
