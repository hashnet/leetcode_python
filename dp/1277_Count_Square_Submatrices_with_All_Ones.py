from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        DP = [[0 for _ in range(n)] for _ in range(m)]

        maxSquares = 0
        for i in range(m):
            DP[i][0] = matrix[i][0]
            maxSquares += DP[i][0]

        for j in range(1, n):
            DP[0][j] = matrix[0][j]
            maxSquares += DP[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    DP[i][j] = min(DP[i-1][j-1], min(DP[i-1][j], DP[i][j-1])) + 1
                    maxSquares += DP[i][j]

        return maxSquares

        # # Below recursive memoised solution also works but it is very slow compared to the bottom up solution
        # memo = {}
        # self.maxSquares = 0

        # def DP(i: int, j: int) -> int:
        #     if (i, j) in memo:
        #         return memo[(i, j)]

        #     if i==0 or j==0:
        #         subTotal = 0
        #     else:
        #         subTotal = min(DP(i-1, j-1), min(DP(i-1, j), DP(i, j-1)))
            
        #     if matrix[i][j] == 1:
        #         subTotal += 1
        #     else:
        #         subTotal = 0
            
        #     self.maxSquares += subTotal
        #     memo[(i, j)] = subTotal
        #     return subTotal

        # DP(len(matrix)-1, len(matrix[0])-1)
        # return  self.maxSquares

if __name__ == "__main__":
    s = Solution()
    print(s.countSquares([[0,0,0],
                          [0,1,0],
                          [0,1,0],
                          [1,1,1],
                          [1,1,0]]))
    print(s.countSquares([[0,1,1,1],
                          [1,1,1,1],
                          [0,1,1,1]]))
    print(s.countSquares([[1,0,1],
                          [1,1,0],
                          [1,1,0]]))
