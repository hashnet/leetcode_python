from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        cRow = len(mat)
        cCol = len(mat[0])
        sum = [[0 for _ in range(cCol+K)] for _ in range(cRow+K)]

        for i in range(cRow):
            for j in range(cCol):
                sum[i][j] = mat[i][j]


        for i in range(cRow+K):
            for j in range(cCol+K):
                if i > 0:
                    sum[i][j] += sum[i-1][j]
                if j > 0:
                    sum[i][j] += sum[i][j-1]
                if i > 0 and j > 0:
                    sum[i][j] -= sum[i-1][j-1]
                    
        span = 2*K+1
        for i in range (cRow+K-1, -1, -1):
            for j in range(cCol+K-1, -1, -1):
                if i >= span:
                    sum[i][j] -= sum[i-span][j]
                if j >= span:
                    sum[i][j] -= sum[i][j-span]
                if i >= span and j >= span:
                    sum[i][j] += sum[i-span][j-span]

        res = [sum[i][K:] for i in range(K,cRow+K)]
        return res

# if __name__ == "__main__":
#     s = Solution()
#     print(s.matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]], 1))
#     print(s.matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]], 2))