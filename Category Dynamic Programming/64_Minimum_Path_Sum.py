from typing import List
from math import inf


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        y = len(grid)
        x = len(grid[0])

        for i in range(1, y):
            grid[i][0] += grid[i-1][0]
        
        for j in range(1, x):
            grid[0][j] += grid[0][j-1]

        for i in range(1, y):
            for j in range(1, x):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[-1][-1]


if __name__ == "__main__":
    s = Solution()
    print(s.minPathSum([[1,3,1], [1,5,1], [4,2,1]]))
