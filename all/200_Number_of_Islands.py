from typing import List

class Solution:
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        R = len(grid)
        if R == 0:
            return 0
        C = len(grid[0])
        
        def DFS(i: int, j: int):
            for (dx, dy) in Solution.dir:
                ni = i + dy
                nj = j + dx
                if ni >= 0 and ni < R and nj >=0 and nj < C and grid[ni][nj] == "1":
                    grid[ni][nj] = "0"
                    DFS(ni, nj)

        count = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1":
                    count += 1
                    grid[i][j] = "0"
                    DFS(i, j)

        return count


if __name__ == "__main__":
    s = Solution()
    print(s.numIslands([["1","1","1","1","0"],
                        ["1","1","0","1","0"],
                        ["1","1","0","0","0"],
                        ["0","0","0","0","0"]]))

    print(s.numIslands([["1","1","0","0","0"],
                        ["1","1","0","0","0"],
                        ["0","0","1","0","0"],
                        ["0","0","0","1","1"]]))
